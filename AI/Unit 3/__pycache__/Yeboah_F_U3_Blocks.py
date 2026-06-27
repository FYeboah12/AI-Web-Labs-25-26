import sys; args = sys.argv[1:]
import re

def is_fit(board, rect, start_x, start_y):
    rect_height, rect_width = rect
    board_height = len(board)
    board_width = len(board[0])

    if start_x + rect_height > board_height or start_y + rect_width > board_width:
        return False

    for i in range(start_x, start_x + rect_height):
        for j in range(start_y, start_y + rect_width):
            if board[i][j] != 0:
                return False

    return True

def place_rect(board, rect, start_x, start_y):
    rect_height, rect_width = rect
    for i in range(start_x, start_x + rect_height):
        for j in range(start_y, start_y + rect_width):
            board[i][j] = 1

def remove_rect(board, rect, start_x, start_y):
    rect_height, rect_width = rect
    for i in range(start_x, start_x + rect_height):
        for j in range(start_y, start_y + rect_width):
            board[i][j] = 0

def find_holes(board):
    holes = []
    visited = [[False] * len(board[0]) for _ in range(len(board))]

    def dfs(x, y, hole):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if not visited[cx][cy] and board[cx][cy] == 0:
                visited[cx][cy] = True
                hole.append((cx, cy))
                for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        stack.append((nx, ny))

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0 and not visited[i][j]:
                hole = []
                dfs(i, j, hole)
                if hole:
                    holes.append(hole)

    return holes

def backtrack(board, list_of_blox, index, order):
    if index == len(list_of_blox):
        return order, find_holes(board)

    rect = list_of_blox[index]
    rect_height, rect_width = rect

    for i in range(len(board)):
        for j in range(len(board[0])):
            if is_fit(board, rect, i, j):
                place_rect(board, rect, i, j)
                order.append(rect)
                result, holes = backtrack(board, list_of_blox, index + 1, order)
                if result:
                    return result, holes
                remove_rect(board, rect, i, j)
                order.pop()

            rotated_rect = (rect_width, rect_height)
            if is_fit(board, rotated_rect, i, j):
                place_rect(board, rotated_rect, i, j)
                order.append(rotated_rect)
                result, holes = backtrack(board, list_of_blox, index + 1, order)
                if result:
                    return result, holes
                remove_rect(board, rotated_rect, i, j)
                order.pop()

    return [], []

def fix_blocks(board_size, list_of_blox):
    board_height, board_width = board_size
    board = [[0] * board_width for _ in range(board_height)]
    order = []
    return backtrack(board, list_of_blox, 0, order)

def main():
   # finditer returns a list of matches: finditer(pattern, subject, options)
   matches = re.finditer(r"(\d+)( |x)(\d+)", ' '.join(args), re.I)
   # group(0) is the entire match, group(1 or higher) is captured
   pairs = [(int(m.group(1)), int(m.group(3)))  for m in matches]
   #pairs = [(8,18),(8,14),(8,4)]
   board_size = pairs[0]   # the first pair is the board size
   print("The rectangles", pairs[1:])
   fixed, holes = fix_blocks(board_size, pairs[1:])

   if not fixed:
        print("No solution")
   else:
        board_height, board_width = board_size
        board = [[0] * board_width for _ in range(board_height)]
        for rect in fixed:
            placed = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if is_fit(board, rect, i, j):
                        place_rect(board, rect, i, j)
                        placed = True
                        break
                if placed:
                    break
        decomp = [f"{p[0]}x{p[1]}" for p in fixed]
        for hole in holes:
            if len(hole) == 1:
                decomp.append("1x1")
            else:
                min_x = min(hole, key=lambda x: x[0])[0]
                max_x = max(hole, key=lambda x: x[0])[0]
                min_y = min(hole, key=lambda x: x[1])[1]
                max_y = max(hole, key=lambda x: x[1])[1]
                hole_width = max_y - min_y + 1
                hole_height = max_x - min_x + 1
                decomp.append(f"{hole_height}x{hole_width}")
        decomp.sort(key=lambda x: (int(x.split('x')[0]), int(x.split('x')[1])))

        print("Decomposition:", ' '.join(decomp))

if __name__ == '__main__':
    main()

#Frances Yeboah, P5, 2027