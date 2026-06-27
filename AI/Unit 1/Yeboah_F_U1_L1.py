import random, time
 
def getInitialState():
   x = "_12345678"
   l = list(x)
   random.shuffle(l)
   y = ''.join(l)
   return y
   
'''precondition: i<j
   swap characters at position i and j and return the new state'''
def swap(state,i,j):
    sl = list(state)
    a = sl[i]
    sl[i] = sl[j]
    sl[j] = a
    return "".join(sl)
   
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state):
   '''your code goes here'''
   children = []
   blank = state.index("_")
   row = blank // 3
   col = blank % 3
   for r,c in [(row, col + 1),(row, col - 1),(row + 1, col),(row - 1, col)]:
      if 0 <= r < 3 and 0 <= c < 3:
         ind = r * 3 + c
         children.append(swap(state,blank,ind)) if blank < ind else children.append(swap(state,ind,blank))
   return children
 
def display_path(n, explored): #key: current, value: parent
   l = []
   while explored[n] != "s": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   print ()
   l = l[::-1]
   for i in l:
      print (i[0:3], end = "   \n")
   print ()
   for j in l:
      print (j[3:6], end = "   \n")
   print()
   for k in l:
      print (k[6:9], end = "   \n\n\n")
   return len(l)
 
'''Find the shortest path to the goal state "_12345678" and
   returns explored and an empty string or "No solution".
   You can make other helper methods, but you must use dictionary for explored.'''
def BFS(initial_state, goal = "_12345678"):
   # goal test is passed? return explored, ""
   
   solution_found = False
   explored = {initial_state: "s"} #
   frontier = [initial_state]
   while len(frontier) > 0 and not solution_found:
      current = frontier.pop(0) 
      if current == goal:
         solution_found = True
         return explored, ""
      for child in generate_children(current):
         if child not in explored:
            frontier.append(child)
            explored[child] = current
            #display_path()
 
   return explored, "No solution"
 
'''Find the path to the goal state "_12345678" and
   returns explored and an empty string or "No solution".
   You can make other helper methods, but you must use dictionary for explored.'''
def DFS(initial_state, goal = "_12345678"):
   # goal test is passed? return explored, ""
   solution_found = False
   explored = {initial_state: "s"} #
   frontier = [initial_state]
   while len(frontier) > 0 and not solution_found:
      current = frontier.pop() 
      if current == goal:
         solution_found = True
      for child in generate_children(current):
         if child not in explored:
            if child == goal:
               solution_found = True
               return explored, ""
            frontier.append(child)
            explored[child] = current
            #display_path()
 
   return explored, "No solution" if not solution_found else explored, ""

def main():
   initial = getInitialState()
   goal = "_12345678"
   # Fun of 8 puzzle
   #initial = "1234567_8"
   #initial = "14725836_"
   #initial = "12345678_"
   #initial = "84765231_"
   start = time.time()
   print ("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   bfs_result = BFS(initial)
   print ("\n\nThe number of nodes explored:", len(bfs_result[0]))
   if bfs_result[1] != "No solution": 
      print ("\nThe shortest path length is :", display_path(goal, bfs_result[0]))
   else:
      print("no solution")
   print ("BFS duration:", time.time() - start)
   start = time.time()
   print ("\n\nDFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   dfs_result = DFS(initial)
   print ("\n\nThe number of nodes explored:", len(dfs_result[0])) 
 #  if dfs_result[1] != "No solution":
  #    print ("\nThe path length is :", display_path(goal, dfs_result[0]))
  # else:
   #   print("no solution")
   print ("DFS duration:", time.time() - start) 
 
if __name__ == '__main__':
   main()