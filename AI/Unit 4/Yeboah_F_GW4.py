import sys; args = sys.argv[1:]
import re
import math

def get_char(dirs):
    if not dirs: return '.'
    s = "".join(sorted(list(dirs)))
    mapping = {
        'U': 'U', 'R': 'R', 'D': 'D', 'L': 'L',
        'RU': 'V', 'DRU': 'W', 'DR': 'S', 'DLR': 'T',
        'DL': 'E', 'DLU': 'F', 'LU': 'M', 'LRU': 'N',
        'DU': '|', 'LR': '-', 'DLRU': '+'
    }
    return mapping.get(s, '?')

def bfs(start_node, adj):
    q = [(start_node, 0)]
    visited = {start_node: 0}
    idx = 0
    while idx < len(q):
        curr, d = q[idx]
        idx += 1
        for nxt in adj[curr]:
            if nxt not in visited:
                visited[nxt] = d + 1
                q.append((nxt, d + 1))
    return visited

def grfParse(args_upper):
    size = int(args_upper[0])
    width = None
    idx = 1
    if len(args_upper) > 1 and args_upper[1].isdigit():
        width = int(args_upper[1])
        idx = 2
    if width is None:
        for w in range(math.ceil(math.sqrt(size)), size + 1):
            if size % w == 0:
                width = w
                break
    height = size // width
    adj = {i: set() for i in range(size)}
    for i in range(size):
        r, c = i // width, i % width
        if r > 0: adj[i].add(i - width)
        if r < height - 1: adj[i].add(i + width)
        if c > 0: adj[i].add(i - 1)
        if c < width - 1: adj[i].add(i + 1)

    rewards = {}
    implied_val = 12.0
    mode = 'G1'
    for cmd in args_upper[idx:]:
        if cmd == 'G0' or cmd == 'G1':
            mode = cmd
        elif m := re.match(r'R:(-?\d+\.?\d*)$', cmd):
            implied_val = float(m.group(1))
        elif m := re.match(r'R(\d+):(-?\d+\.?\d*)$', cmd):
            rewards[int(m.group(1))] = float(m.group(2))
        elif m := re.match(r'R(\d+)$', cmd):
            rewards[int(m.group(1))] = implied_val
        elif m := re.match(r'B(\d+)([NSEW]*)$', cmd):
            cell, directions = int(m.group(1)), m.group(2)
            r, c = cell // width, cell % width
            if not directions:
                targets = list(adj[cell])
                for t in targets:
                    adj[cell].discard(t)
                    adj[t].discard(cell)
            else:
                for char in directions:
                    t = -1
                    if char == 'N' and r > 0: t = cell - width
                    elif char == 'S' and r < height - 1: t = cell + width
                    elif char == 'E' and c < width - 1: t = cell + 1
                    elif char == 'W' and c > 0: t = cell - 1
                    if t != -1:
                        if t in adj[cell]:
                            adj[cell].discard(t)
                            adj[t].discard(cell)
                        else:
                            adj[cell].add(t)
                            adj[t].add(cell)
    return size, width, adj, rewards, mode

def main():
    args_upper = [arg.upper() for arg in args]
    size, width, adj, rewards, mode = grfParse(args_upper)
    dist_maps = {r_idx: bfs(r_idx, adj) for r_idx in rewards}

    output = []
    for i in range(size):
        if i in rewards:
            output.append('*')
            continue

        best_score = None
        best_rewards = []

        for r_idx, r_val in rewards.items():
            if i not in dist_maps[r_idx]:
                continue
            d = dist_maps[r_idx][i]
            if d == 0:
                continue 
            if mode == 'G0':
                score = (r_val, -d) 
            else:  # G1
                score = r_val / d

            if best_score is None or score > best_score:
                best_score = score
                best_rewards = [(r_idx, d)]
            elif score == best_score:
                best_rewards.append((r_idx, d))

        if best_score is None:
            output.append('.')
            continue

        found_dirs = set()
        for nxt in adj[i]:
            for r_idx, d in best_rewards:
                nxt_dist = dist_maps[r_idx].get(nxt)
                if nxt_dist is not None and nxt_dist == d - 1:
                    if nxt == i - width: found_dirs.add('U')
                    elif nxt == i + width: found_dirs.add('D')
                    elif nxt == i - 1: found_dirs.add('L')
                    elif nxt == i + 1: found_dirs.add('R')
                    break 

        output.append(get_char(found_dirs))

    print("".join(output))

if __name__ == '__main__':
    main()

#Frances Yeboah, P5, 2027