# Name: Frances Yeboah P5
# Date: 11/14/25
import random

class RandomPlayer: #picks truly random moves, not optimal ones
   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 5
      self.y_max = 5
      self.first_turn = True
      
   def best_strategy(self, board, color):
      # Terminal test: when there's no more possible move
      #                return (-1, -1), 0
      # returns best move
      # (column num, row num), 0
      if len(self.find_moves(board,color)) == 0:
         return (-1,-1),0
      possibles = list(self.find_moves(board,color))
      best_move = possibles[random.randint(0,len(possibles)-1)] #get random val
      #x and y
      #print("X:",best_move % 5,"Y:",(best_move - (best_move % 5) // 5))
      print("col:",best_move // 5,"row:",best_move % 5)
      return (best_move // 5, best_move % 5), 0
      
     
   def find_moves(self, board, color):
      # finds all possible moves
      # returns a set, e.g., {0, 1, 2, 3, ...., 24} 
      # 0 5 10 15 20
      # 1 6 11 16 21
      # 2 7 12 17 22
      # 3 8 13 18 23
      # 4 9 14 19 24
      # if 2 has 'X', board = [['.', '.', 'X', '.', '.'], [col 2], .... ]
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

class CustomPlayer: #chooses optimal value

   def __init__(self):
      self.white = "#ffffff" #"O" #min
      self.black = "#000000" #"X" #max
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 5
      self.y_max = 5
      self.first_turn = True

   def best_strategy(self, board, color):
      # returns best move
      og_board = [[] for x in range(5)]
      for x in range(5):
            for y in range(5):
               og_board[x].append(board[x][y])
      if len(self.find_moves(board,color)) == 0:
         return (-1,-1),0      
      best_move = self.minimax(og_board,color,2) #change
      #col, row, 0
      self.first_turn = False
      return (best_move[1] % 5,best_move[1] // 5 ), 1

   def minimax(self, board, color, search_depth):
      # search_depth: start from 2
      # returns best "value"
      #(utility,board),move
      if len(self.find_moves(board,color)) == 0: return (self.evaluate(board,color,self.find_moves(board,color)), board),-1
      elif search_depth > 25: return (self.evaluate(board,color,self.find_moves(board,color)),board),-1
      possible_moves = self.find_moves(board,color)
      if color == self.black:
         best_val = -99999
         best_move = (-1,board),-1
         v = (-999999, board),-1
         for move in possible_moves:
            new_board = self.make_move(board,color,move)
            v = max(v,self.minimax(new_board,self.white,search_depth + 1))
            if v[0][0] > best_val:
               best_val = v[0][0]
               best_move = move
         return v[0],best_move
      if color == self.white:
         best_move = (-1,board),-1
         best_val = 99999
         v = (999999, board), -1
         for move in possible_moves:
            new_board = self.make_move(board,color,move)
            v = min(v,self.minimax(new_board,self.black,search_depth + 1))
            if v[0][0] < best_val:
               best_val = v[0][0]
               best_move = move
         return v[0],best_move      
      return v[0],best_move
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      pass

   def make_move(self, board, color, move):
      # returns board that has been updated
      new_board = board[:]
      move_x, move_y = move // 5, move % 5
      new_board[move_x][move_y] = 'X' if color == self.black else 'O'
      return new_board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      # count possible_moves (len(possible_moves)) of my turn at current board
      # opponent's possible_moves: self.find_moves(board, self.opposite_color(color))
      return len(possible_moves) - len(self.find_moves(board, self.opposite_color[color]))

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

# x = move // 5
# y = move % 5
# move = x * 5 + y

'''
def max_value(state, turn, tc):
   #compare val and state
   # return value and state: (val, state)
   other_turn = 'O' if turn == 'X' else 'X'
   if terminal_test(state,tc): return (utility(turn,tc,state),state)
   v = (-99999,state)
   #next_state = state
   for a, s in successors(state,turn):
      v = max(v,min_value(s,other_turn,tc))
      #if v[1] > next_state: next_state = v[1]
      if v[0] == -1: return v
   return 1,state 
   
def min_value(state, turn, tc):
   # return value and state: (val, state)
   other_turn = 'O' if turn == 'X' else 'X'
   if terminal_test(state,tc): return (utility(turn,tc,state),state)
   v = (99999,state)
   #next_state = state
   for a, s in successors(state,turn):
      v = min(v,max_value(s,other_turn,tc))
      #if v[1] < next_state: next_state = v[1]
      if v[0] == 1: return v
   return -1,state   
'''