# Name: Frances Yeboah    Date: 9/3/25
import time

def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()
   # TODO 1: adjacents
   # Your code goes here
   og_current = current
   compare_current = list(current)
   alpha = "abcdefghijklmnopqrstuvwxyz"
   for x in range(len(current)):
      for let in alpha:
         compare_current[x] = let
         check_word = "".join(compare_current)
         if check_word in words_set and check_word != og_current: adj_set.add(check_word)
      compare_current = list(current)
   #adj_set.add(word for word in words_set if )
   return adj_set

def check_adj(words_set):
   # This check method is written for words_6_longer.txt
   adj = generate_adjacents('listen', words_set)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)

def bi_bfs(start, goal, words_set):
   '''The idea of bi-directional search is to run two simultaneous searches--
   one forward from the initial state and the other backward from the goal--
   hoping that the two searches meet in the middle. 
   '''
   if start == goal: return []
   # TODO 2: Bi-directional BFS Search
   # Your code goes here
   front_explored = {start: "s"}
   back_explored = {goal: "end"}
   front_ier = [start]
   back_ier = [goal]
   while front_ier and back_ier:
      if len(front_ier) > 0:
         current_front  = front_ier.pop(0)
         if current_front in back_ier: 
            #front_explored[goal] = current_front
            #return path(goal,front_explored)
            return path(current_front, front_explored, back_explored)
         for child in generate_adjacents(current_front, words_set):
            if child not in front_explored:
               front_ier.append(child)
               front_explored[child] = current_front
      if len(back_ier) > 0:
         current_back = back_ier.pop(0)
         if current_back in front_ier:
            front_explored[goal] = current_back
            #print("current (key):", front_explored[goal], "parent (value)", current_back)
            #return path(goal,front_explored)
            return path(current_back, front_explored, back_explored)
         for child in generate_adjacents(current_back, words_set):
            if child not in back_explored:
               back_ier.append(child)
               back_explored[child] = current_back
   return None
#dict[key] = val
#key = current, val = parent
def path(match, front, back):
   og_match = match
   # path = []
   # while front[match] != "s":
   #    path.append(match)
   #    match = front[match]
   # path.append(match)
   # path = path[::-1]
   # match = og_match
   # while back[match] != "end":
   #    if match != og_match:
   #       path.append(match)
   #    match = back[match]
   # path.append(match)
   # return path
   front_path = []
   back_path  = []
   path = []
   while front[match] != "s":
      front_path.append(match)
      match = front[match]
   front_path.append(match)
   front_path = front_path[::-1]
   match  = og_match
   while back[match] != "end":
      if match != og_match:
         back_path.append(match)
      match = back[match]
   back_path.append(match)
   #back_path = back_path[::-1]
   path = front_path + back_path
   return path
   

   # while(exp[state] != "s"):
   #    path.append(state)
   #    state = exp[state]
   # path.append(state)
   # return path[::-1]

def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   #print(generate_adjacents("copier",words_set))
   #print ("Check generate_adjacents():", check_adj(words_set))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   path = (bi_bfs(initial, goal, words_set))
   if path != None:
      print (path)
      print ("The number of steps: ", len(path))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''


