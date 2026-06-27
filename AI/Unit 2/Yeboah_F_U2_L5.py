import sys; args = sys.argv[1:]
import re

def can_place_block(board, block, position):
    block_h, block_w = block
    max_h, max_w = len(board), len(board[0])
    if position[0] + block_h > max_h or position[1] + block_w > max_w:
        return False
    for i in range(position[0], position[0] + block_h):
        for j in range(position[1], position[1] + block_w):
            if board[i][j] != 0:
                return False
    return True

def place_block(board, block, position):
    block_h, block_w = block
    for i in range(position[0], position[0] + block_h):
        for j in range(position[1], position[1] + block_w):
            board[i][j] = (block_h,block_w)

def remove_block(board, block, position):
    block_h, block_w = block
    for i in range(position[0], position[0] + block_h):
        for j in range(position[1], position[1] + block_w):
            board[i][j] = 0 

def fix_blocks(board, blocks, block_index, order):
    if block_index == len(blocks):
        return order
    block = blocks[block_index]
    block_h, block_w = block
    board_height, board_width = len(board), len(board[0])
    #og orientation
    for i in range(board_height):
        for j in range(board_width):
            if can_place_block(board, block, (i, j)):
                place_block(board, block, (i, j))
                order.append((block, (i, j)))
                result = fix_blocks(board, blocks, block_index + 1, order)
                if result:
                    return result
                remove_block(board, block, (i, j))
                order.pop()

            # rotate
            if block_h != block_w:
                rotated_block = (block_w, block_h)
                if can_place_block(board, rotated_block, (i, j)):
                    place_block(board, rotated_block, (i, j))
                    order.append((rotated_block, (i, j)))
                    result = fix_blocks(board, blocks, block_index + 1, order)
                    if result:
                        return result
                    remove_block(board, rotated_block, (i, j))
                    order.pop()
   
    return []

def flood_fill(board, visited, start_i, start_j):
    stack = [(start_i, start_j)]
    visited[start_i][start_j] = True
    cells = [(start_i, start_j)]

    while stack:
        i, j = stack.pop()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and not visited[ni][nj] and board[ni][nj] == 0:
                visited[ni][nj] = True
                stack.append((ni, nj))
                cells.append((ni, nj))

    return cells

def find_holes(board):
    visited = [[False] * len(board[0]) for x in range(len(board))]
    holes = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0 and not visited[i][j]:
                cells = flood_fill(board, visited, i, j)
                min_i = min(cells, key=lambda x: x[0])[0]
                max_i = max(cells, key=lambda x: x[0])[0]
                min_j = min(cells, key=lambda x: x[1])[1]
                max_j = max(cells, key=lambda x: x[1])[1]
                hole_height = max_i - min_i + 1
                hole_width = max_j - min_j + 1
                holes.append(((hole_height, hole_width), (min_i, min_j)))

    return holes

def main():
   # finditer returns a list of matches: finditer(pattern, subject, options)
   #matches = re.finditer(r"(\d+)( |x)(\d+)", "13 18 8 1 8 4 5 10 8 18", re.I)
   matches = re.finditer(r"(\d+)( |x)(\d+)", ' '.join(args), re.I)
   # group(0) is the entire match, group(1 or higher) is captured
   pairs = [(int(m.group(1)), int(m.group(3)))  for m in matches]
   board_size = pairs[0]   # the first pair is the board size  
   board = [[0] * board_size[1] for x in range(board_size[0])]
   #decomp = [str(p[0])+"x"+str(p[1]) for p in pairs[1:]]
   blocks = sorted(pairs[1:], key=lambda x: x[0] * x[1], reverse=True)
   solution = fix_blocks(board, blocks, 0, [])
   if solution == []:
        print("No solution")
   else:
        # how you are supposed to print the solution
        holes = find_holes(board)
        all = solution + holes
        all.sort(key=lambda x: (x[1][0], x[1][1]))
        decomp = [str(p[0])+"x"+str(p[1]) for p, pos in all]
        print("Decomposition:", " ".join(decomp))   

if __name__ == '__main__': main()
#def fix_blocks(board_size,blocks):
#    #account for holes
   
#    board_height = board_size[0]
#    board_width = board_size[1]
#    board_area = board_height * board_width
#    blocks_to_areas = {block[0] * block[1]: block for block in blocks}
#    full_board = [[0 for col in range(board_width)] for row in range(board_height)]
#    #print(full_board)
#    #special case: make it into sections instead of subtracting from the original
#    order = []
#    blocks = sorted(blocks_to_areas.keys(), reverse=True)
#    blocks = [blocks_to_areas[x] for x in blocks]
#    for block in blocks:
#       cur_block_h = block[0]
#       cur_block_w = block[1]
#       #case 1: block fits in quite perfectly
#       if (cur_block_h * cur_block_w) <= board_area and (cur_block_h == board_height) and (cur_block_w <= board_width):
#          order.append(block)
#          board_area -= cur_block_h * cur_block_w
#          board_width -= cur_block_w 
#       elif (cur_block_h * cur_block_w) <= board_area and (cur_block_h <= board_height) and (cur_block_w == board_width):
#          order.append(block)
#          board_area -= cur_block_h * cur_block_w
#          board_height -= cur_block_h #account for less dimensions? 
#       #case 2: block fits in "perfectly"- as in h and w is less than or equal to og, area is less than or equal to og
#       elif (cur_block_h * cur_block_w) <= board_area and (cur_block_h <= board_height) and (cur_block_w <= board_width):
#          order.append(block)
#          board_area -= cur_block_h * cur_block_w
#          board_height -= cur_block_h #account for less dimensions?
#          board_width -= cur_block_w
         
#       #case 3: block needs rotation
#       elif (cur_block_h * cur_block_w) <= board_area and (cur_block_h <= board_width) and (cur_block_w <= board_height):
#          order.append((cur_block_w,cur_block_h))
#          board_area -= cur_block_h * cur_block_w
#          board_height -= cur_block_w
#          board_width -= cur_block_h
#       #case 4: block does not fit
#       else:
#          return []
#    if len(order) != len(blocks): return []  
#    return order #list of the order of blocks in the board

# '''
# def bruteforce(pzl,...):
#    if done: return pzl
#    find set of chocies:
#    for each choice:
#       newpzl = pzl w/ choice applied
#       bf = bruteforce(newpzl,...)
#       if bf: return bf
#    return None
# '''

# def fix_blocks_recur(og_board_dims,board_area,blocks,og_len, order):
#    if len(order) >= og_len: return order #if done ret pzl
#    #array representation
#    #set of choices: the individual block and it's reverse 
#    avail_board_height = og_board_dims[0]
#    avail_board_width = og_board_dims[1]
#    for i in range(len(blocks)):
#       order.append(blocks[i])
#       #check blocks
#       block = blocks[i]
#       cur_block_h = block[0]
#       cur_block_w = block[1]
#       #case 1: block fits in quite perfectly
#       if (cur_block_h * cur_block_w) <= board_area and (cur_block_h == avail_board_height) and (cur_block_w <= avail_board_width):
#          board_area -= cur_block_h * cur_block_w
#       elif (cur_block_h * cur_block_w) <= board_area and (cur_block_h <= avail_board_height) and (cur_block_w == avail_board_width):
#          board_area -= cur_block_h * cur_block_w 
#       #case 2: block fits in "perfectly"- as in h and w is less than or equal to og, area is less than or equal to og
#       elif (cur_block_h * cur_block_w) <= board_area and (cur_block_h <= avail_board_height) and (cur_block_w <= avail_board_width):
#          board_area -= cur_block_h * cur_block_w  
#       #case 3: block needs rotation
#       elif (cur_block_h * cur_block_w) <= board_area and (cur_block_h <= avail_board_width) and (cur_block_w <= avail_board_height):
#          order.pop()
#          order.append((cur_block_w,cur_block_h))
#          board_area -= cur_block_h * cur_block_w
#       #case 4: block does not fit 
#       else: return False      
#       valid = fix_blocks_recur(og_board_dims,board_area,blocks[i+1:],og_len,order)
#       if valid: return valid
#       return []
#    return None
    
#Frances Yeboah, P5, 2027