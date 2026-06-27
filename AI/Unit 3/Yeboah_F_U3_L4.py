# Name: Frances Yeboah P5
# Date: 12/14/25
 
global static_weights
global hash_table
class Best_AI_bot: #done?
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
 
   def best_strategy(self, board, color):
    # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      #this is very important *skull emoji*
      if color == "#000000":
         color = "@"
      else:
         color = "O"      
      if self.stones_left(board) > 0:
         self.static_weight()
         og_board = [[] for x in range(8)]
         for x in range(len(board)):
            for y in range(len(board[0])):
               og_board[x].append(board[x][y])
         best_move = self.minimax(og_board,color,2)
         #best_move = self.alphabeta(og_board,color,2,-9999,9999)
         #board is the problem
         #print("before assignment (utility, board, position)",best_move)
         best_move = best_move[1]
         if best_move >= 0:
            return [best_move // 8, best_move % 8], 0
         
   def minimax(self, board, color, search_depth): #returns (utility value, board), place on board
    # returns best "value"
      possible_moves = self.find_moves(board,color)
      if len(possible_moves) == 0: return (self.evaluate(board,color,possible_moves), board),-1
      elif search_depth > 6: return (self.evaluate(board,color,possible_moves),board),-1
      if color == self.black:
         best_val = -9999
         best_move = -1
         v = (-9999, board[:]),-1
         for move in possible_moves: #key, number
            new_board = self.make_move(board[:],color,move,self.find_flipped(board,move // 8, move % 8, color))
            v = max(v,self.minimax(new_board,self.white,search_depth + 1))
            if v[0][0] > best_val:
               best_val = v[0][0]
               best_move = move
         return (v[0][0],board),best_move
      if color == self.white:
         best_move = -1
         best_val = 9999
         v = (9999, board[:]), -1
         for move in possible_moves:
            new_board =  self.make_move(board[:],color,move,self.find_flipped(board,move // 8, move % 8, color))
            v = min(v,self.minimax(new_board,self.black,search_depth + 1))
            if v[0][0] < best_val:
               best_val = v[0][0]
               best_move = move
         return (v[0][0],board),best_move      
      return (v[0][0],board),best_move     
 
   def negamax(self, board, color, search_depth):
    # returns best "value"
      pass
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
    # returns best "value" while also pruning
      possible_moves = self.find_moves(board,color)
      if len(possible_moves) == 0: return (self.evaluate(board,color,possible_moves), board),-1
      elif search_depth > 5: return (self.evaluate(board,color,possible_moves),board),-1
      if color == self.black:
         best_val = -9999
         best_move = -1
         v = (-9999, board[:]),-1
         for move in possible_moves: #key, number
            new_board = self.make_move(board[:],color,move,self.find_flipped(board,move // 8, move % 8, color))
            v = max(v,self.alphabeta(new_board,self.white,search_depth + 1,alpha,beta))
            if v[0][0] < beta:
               best_val = v[0][0]
               best_move = move
               return (best_val,board),best_move
            alpha = max(alpha,v[0][0])
      if color == self.white:
         best_val = 9999
         best_move = -1
         v = (9999, board[:]), -1
         for move in possible_moves:
            new_board =  self.make_move(board[:],color,move,self.find_flipped(board,move // 8, move % 8, color))
            v = min(v,self.alphabeta(new_board,self.black,search_depth + 1,alpha,beta))
            if v[0][0] > alpha:
               best_val = v[0][0]
               best_move = move
               return (best_val,board),best_move
            beta = min(beta,v[0][0])
      return v 
 
   def make_key(self):
    # hashes the board
      #i'll make it correspond with the othello board in schoology so the column numbers goes to 63
      hashes = {x:(x // 8, x % 8) for x in range(64)}
      return hashes
   
   def static_weight(self):
      global static_weights
      global hash_table
      static_weights = [] #col order
      static_weights.append([4,-3,2,2,2,2,-3,4])
      static_weights.append([-3,-4,-1,-1,-1,-1,-4,-3])
      static_weights.append([2,-1,1,0,0,1,-1,2])
      static_weights.append([2,-1,0,1,1,0,-1,2])
      static_weights.append([2,-1,0,1,1,0,-1,2])
      static_weights.append([2,-1,1,0,0,1,-1,2])
      static_weights.append([-3,-4,-1,-1,-1,-1,-4,-3])
      static_weights.append([4,-3,2,2,2,2,-3,4])
      hash_table = self.make_key()
 
   def stones_left(self, board):
    # returns number of stones that can still be placed
      stones_left = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == ".":
               stones_left += 1
      return stones_left
 
   def make_move(self, board, color, move, flipped):
    # returns board that has been updated
      new_board = board[:]
      move = (move // 8, move % 8)
      new_board[move[1]][move[0]] = color #make moves and flip
      for flip in flipped:
         new_board[flip[1]][flip[0]] = color
      return new_board
 
   def evaluate(self, board, color, possible_moves):
    # returns the utility value
      #cur_color possible moves - opp_color possible moves (not enough)
      return 10 * self.corner_heuristic(board, color, possible_moves) + 5 * self.mobility_heuristic(board, color, possible_moves) + 5 * self.stability_heuristic(board, color, possible_moves)
 
   def score(self, board, color):
    # returns the score of the board 
      score = 0
      for x in range(self.x_max):
         for y in range(self.y_max):
            if board[x][y] == color:
               score += 1
      return 1
 
   def find_moves(self, board, color):
    # finds all possible moves
    moves_found = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                moves_found.update({i*self.y_max+j: flipped_stones})
    return moves_found
 
   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
    if board[x][y] != ".":
        return []
    flipped_stones = []
    for incr in self.directions:
        temp_flip = []
        x_pos = x + incr[0]
        y_pos = y + incr[1]
        while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if board[x_pos][y_pos] == ".":
                break
            if board[x_pos][y_pos] == color:
                flipped_stones += temp_flip
                break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
    return flipped_stones 
   
   #use sum of static weights of each possible value (heuristic article in schoology)
   #avoid opponents best move, not find my best mvoe
   #-2 * (s.o.s.w.o.e opp's poss moves)
   #different strategy for beg, mid, end
   
   def mobility_heuristic(self, board, color, possible_moves): #available moves
      return -2 * len(self.find_moves(board,self.opposite_color))
   
   def corner_heuristic(self, board, color, possible_moves): #corners captured
      #0,7,56, and 63 are corners
      score = 0
      for m in possible_moves:
         if m in [0,7,56,63]:
            score += 100
      for m in self.find_moves(board,self.opposite_color):
         if m in [0,7,56,63]:
            score -= 1000
      return score
 
   def stability_heuristic(self, board, color, possible_moves):
      global static_weights
      global hash_table
      sum = 0
      for move in possible_moves:
         col, row = hash_table[move]
         sw = static_weights[row][col]
         sum += sw
      return sum
