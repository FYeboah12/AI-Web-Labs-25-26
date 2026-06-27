import sys; args = sys.argv[1:]
import re
import math

edge_lookup = {
    'J': {'N', 'W'}, 'N': {'N'}, '^': {'E', 'N', 'W'}, 'L': {'E', 'N'},
    '<': {'N', 'S', 'W'}, 'W': {'W'}, '+': {'E', 'N', 'S', 'W'}, 'E': {'E'},
    '>': {'E', 'N', 'S'}, '7': {'S', 'W'}, 'v': {'E', 'S', 'W'}, 'S': {'S'},
    'r': {'E', 'S'}, '-': {'E', 'W'}, '|': {'N', 'S'}, '.': set()
}

def get_indices(slice_str, size, width):
    clean_str = re.split('[BRT]', slice_str, flags=re.I)[0]
    result = []
    for part in clean_str.split(','):
        if not part: continue
        if '#' in part:
            parts = part.split('#')
            v1 = (int(parts[0]) + size) % size if parts[0] else 0
            v2 = (int(parts[1]) + size) % size if parts[1] else size - 1
            if width > 0:
                r1, c1, r2, c2 = v1 // width, v1 % width, v2 // width, v2 % width
                for r in range(min(r1, r2), max(r1, r2) + 1):
                    for c in range(min(c1, c2), max(c1, c2) + 1):
                        idx = r * width + c
                        if idx < size: result.append(idx)
            else:
                step = 1 if v1 <= v2 else -1
                result.extend(range(v1, v2 + step, step))
        elif ':' in part:
            p = [(int(x) if x else None) for x in part.split(':')]
            result.extend(range(size)[slice(*p)])
        else:
            result.append((int(part) + size) % size)
    return result

def grfParse(lstArgs):
    g_match = re.match('G(G|N)?(\d+)(?:W(\d+))?(?:R(\d+))?', lstArgs[0], re.I)
    g_type = g_match.group(1).upper() if g_match.group(1) else 'G'
    size = int(g_match.group(2))
    def_rwd = int(g_match.group(4)) if g_match.group(4) else 12
    width = 0
    if g_type == 'G':
        if g_match.group(3): width = int(g_match.group(3))
        else:
            root = math.ceil(math.sqrt(size))
            width = next(w for w in range(root, size + 1) if size % w == 0)
    edges = set()
    if width > 0:
        for v in range(size):
            r, c = v // width, v % width
            if r > 0: edges.add((v, v - width))
            if r < (size // width) - 1: edges.add((v, v + width))
            if c < width - 1: edges.add((v, v + 1))
            if c > 0: edges.add((v, v - 1))
    v_props, e_props = {}, {}
    for arg in lstArgs[1:]:
        if arg.startswith('V'):
            W = get_indices(arg[1:], size, width)
            W_set = set(W)
            if 'B' in arg.upper():
                X = set(range(size)) - W_set
                B = {(w, x) for w in W_set for x in X} | {(x, w) for w in W_set for x in X}
                N_B = set()
                if width > 0:
                    for u, v in B:
                        if abs(u//width - v//width) + abs(u%width - v%width) == 1: N_B.add((u, v))
                to_rem = edges & B
                edges -= to_rem
                edges |= (N_B - to_rem)
                for e in to_rem: e_props.pop(e, None)
            if 'R' in arg.upper():
                r_m = re.search(r'R(\d*)', arg, re.I)
                val = int(r_m.group(1)) if r_m.group(1) else def_rwd
                for v in W_set: v_props[v] = {'rwd': val}
        elif arg.startswith('E'):
            mng = arg[1] if arg[1] in "~!+*@" else "~"
            body = arg[2:] if arg[1] in "~!+*@" else arg[1:]
            r_m = re.search(r'R(\d*)', body, re.I)
            rwd = int(r_m.group(1)) if r_m and r_m.group(1) else (def_rwd if r_m else None)
            if r_m: body = body[:r_m.start()]
            e_set_input = set()
            d_m = re.search(r'([NSEW]+)([=~])', body, re.I)
            if d_m:
                dirs, op = d_m.group(1).upper(), d_m.group(2)
                W = get_indices(body[:d_m.start()], size, width)
                for v in W:
                    for d in dirs:
                        nb = None
                        if d == 'N' and v >= width: nb = v - width
                        elif d == 'S' and v < size - width: nb = v + width
                        elif d == 'E' and (v + 1) % width != 0: nb = v + 1
                        elif d == 'W' and v % width != 0: nb = v - 1
                        if nb is not None:
                            e_set_input.add((v, nb))
                            if op == '=': e_set_input.add((nb, v))
            else:
                conn = re.search(r'[=~]', body)
                if conn:
                    op = conn.group()
                    v1s, v2s = get_indices(body.split(op)[0], size, width), get_indices(body.split(op)[1], size, width)
                    for v1, v2 in zip(v1s, v2s):
                        e_set_input.add((v1, v2))
                        if op == '=': e_set_input.add((v2, v1))
            if mng == '!':
                for e in e_set_input:
                    edges.discard(e)
                    e_props.pop(e, None)
            elif mng == '~':
                for e in e_set_input:
                    if e in edges:
                        edges.remove(e)
                        e_props.pop(e, None)
                    else:
                        edges.add(e)
                        if rwd is not None: e_props[e] = {'rwd': rwd}
            elif mng == '+':
                for e in e_set_input:
                    if e not in edges:
                        edges.add(e)
                        if rwd is not None: e_props[e] = {'rwd': rwd}
            elif mng == '*':
                for e in e_set_input:
                    edges.add(e)
                    if rwd is not None: e_props[e] = {'rwd': rwd}
            elif mng == '@':
                for e in e_set_input:
                    if e in edges and rwd is not None: e_props[e] = {'rwd': rwd}
    return [size, width, def_rwd, edges, v_props, e_props, g_type]

def grfSize(g): return g[0]
def grfGProps(g):
    p = {'rwd': g[2]}
    if g[6] != "N": p['width'] = g[1]
    return p
def grfNbrs(g, v): return sorted([nb for src, nb in g[3] if src == v])
def grfVProps(g, v): return g[4].get(v, {})
def grfEProps(g, v1, v2): return g[5].get((v1, v2), {})

def grfStrEdges(g):
    size, width, edges = g[0], g[1], g[3]
    grid, jumps = [], []
    if width > 0:
        for v in range(size):
            r, c, actual = v // width, v % width, {nb for src, nb in edges if src == v}
            d_s = set()
            if (v-width) in actual and r > 0: d_s.add('N')
            if (v+width) in actual and r < (size//width)-1: d_s.add('S')
            if (v+1) in actual and c < width-1: d_s.add('E')
            if (v-1) in actual and c > 0: d_s.add('W')
            grid.append(next((s for s, d in edge_lookup.items() if d == d_s), '.'))
    for v1, v2 in edges:
        is_nat = width > 0 and (abs(v1-v2) == width or (abs(v1-v2) == 1 and v1//width == v2//width))
        if not is_nat or v1 == v2:
            if (v2, v1) in edges and v1 != v2:
                if v1 < v2: jumps.append((v1, v2, '='))
            else:
                jumps.append((v1, v2, '~'))
    res = "".join(grid)
    if jumps:
        uj = sorted(list(set(jumps)))
        jp = []
        for op in ['=', '~']:
            f = [j for j in uj if j[2] == op]
            if f:
                s_list = [str(j[0]) for j in f]
                d_list = [str(j[1]) for j in f]
                jp.append(",".join(s_list) + op + ",".join(d_list))
        res += ("\nJumps: " if width > 0 else "Jumps: ") + ";".join(jp)
    return res

def grfStrProps(g):
    gp = grfGProps(g)
    out = [f"rwd: {gp['rwd']}, width: {gp['width']}"] if 'width' in gp else [f"rwd: {gp['rwd']}"]
    grps = {}
    for v, p in g[4].items(): grps.setdefault(f"rwd: {p['rwd']}", []).append(v)
    for e, p in g[5].items(): grps.setdefault(f"rwd: {p['rwd']}", []).append(e)
    for ps in sorted(grps.keys(), key=lambda x: int(x.split(': ')[1])):
        keys = grps[ps]
        vk = sorted([str(k) for k in keys if isinstance(k, int)], key=int)
        ek = sorted([f"({k[0]}, {k[1]})" for k in keys if isinstance(k, tuple)])
        out.append(f"{', '.join(vk + ek)}: {ps}")
    return "\n".join(out)


def formatEdges(size, width, edgesStr):
    if width <= 0: return edgesStr
    parts = edgesStr.split('\n')
    grid = "\n".join([parts[0][i:i+width] for i in range(0, len(parts[0]), width)])
    return grid + ("\n" + parts[1] if len(parts) > 1 else "")

def main():
    graph = grfParse(args)
    edges_str = grfStrEdges(graph)
    props_str = grfStrProps(graph)
    print(grfGProps(graph))
    print(formatEdges(graph[0], graph[1], edges_str))
    print(props_str)

if __name__ == '__main__':
    main()
#Frances Yeboah, P5, 2025