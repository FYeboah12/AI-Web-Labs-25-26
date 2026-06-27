import random

class RandomPlayer:
    def __init__(self):
        self.white = "#ffffff"
        self.black = "#000000"
        self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        self.opposite_color = {self.black: self.white, self.white: self.black}
        self.x_max = 5
        self.y_max = 5
        self.first_turn = True

    def best_strategy(self, board, color):
        moves = self.find_moves(board, color)
        if moves:
            return random.choice(list(moves)), 0
        return (-1, -1), 0

    def find_moves(self, board, color):
        moves = set()
        for i in range(self.x_max):
            for j in range(self.y_max):
                if board[i][j] == '.':
                    moves.add((i, j))
        return moves

class CustomPlayer:
    def __init__(self):
        self.white = "#ffffff"
        self.black = "#000000"
        self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        self.opposite_color = {self.black: self.white, self.white: self.black}
        self.x_max = 5
        self.y_max = 5
        self.first_turn = True

    def best_strategy(self, board, color):
      if len(self.find_moves(board,color)) == 0:
         return (-1,-1),0
      best_move = self.minimax(board,color,2) #change
      #col, row, 0
      self.first_turn = False
      return (best_move[1] % 5,best_move[1] // 5 ), 1

    def minimax(self, board, color, search_depth):
        if search_depth == 0:
            return None, 0
        moves = self.find_moves(board, color)
        best_value = -9999
        best_move = None
        for move in moves:
            new_board = self.make_move(board, color, move)
            value = -self.minimax(new_board, self.opposite_color[color], search_depth - 1)[1]
            if value > best_value:
                best_value = value
                best_move = move
        return best_move, best_value

    def negamax(self, board, color, search_depth):
        if search_depth == 0:
            return None, 0
        moves = self.find_moves(board, color)
        best_value = -99999
        best_move = None
        for move in moves:
            new_board = self.make_move(board, color, move)
            value = -self.negamax(new_board, self.opposite_color[color], search_depth - 1)[1]
            if value > best_value:
                best_value = value
                best_move = move
        return best_move, best_value

    def alphabeta(self, board, color, search_depth, alpha, beta):
        if search_depth == 0:
            return None, 0
        moves = self.find_moves(board, color)
        best_value = -99999
        best_move = None
        for move in moves:
            new_board = self.make_move(board, color, move)
            value = -self.alphabeta(new_board, self.opposite_color[color], search_depth - 1, -beta, -alpha)[1]
            if value > best_value:
                best_value = value
                best_move = move
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
        return best_move, best_value

    def make_move(self, board, color, move):
        x, y = move // 5, move % 5
        new_board = [row[:] for row in board]
        new_board[x][y] = color
        return new_board

    def evaluate(self, board, color, possible_moves):
        my_moves = len(possible_moves)
        opponent_moves = len(self.find_moves(board, self.opposite_color[color]))
        return my_moves - opponent_moves

    def find_moves(self, board, color):
      # finds all possible moves
        moves_found = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.first_turn == True and board[i][j] == '.': 
                    moves_found.add(i*self.y_max+j)
                elif (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
                    for incr in self.directions:
                        x_pos = i + incr[0]
                        y_pos = j + incr[1]
                        stop = False
                        while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                            if board[x_pos][y_pos] != '.':
                                stop = True
                            if not stop:    
                                moves_found.add(x_pos*self.y_max+y_pos)
                            x_pos += incr[0]
                            y_pos += incr[1]
        return moves_found

