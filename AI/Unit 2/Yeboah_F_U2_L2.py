# Name: Frances Yeboah
# Date: 10/1/25
def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for hexa in csp_table:
      if len(set([assignment[i] for i in hexa])) != 6: return False
   return True
   
def select_unassigned_var(assignment, csp_table):
   """ your code goes here """
   count = 0
   most_count = 0
   most_const_index = -1
   for i in range(len(assignment)):
      for r in range(len(csp_table)):
         for c in range(len(csp_table[0])):
               if csp_table[r][c] == i and assignment[i] == ".":
                  count += 1
      if count > most_count and count > 0: 
         most_count = count
         most_const_index = i
      count = 0
      
   return most_const_index
 
def isValid(value, var_index, assignment, csp_table):
   """ your code goes here """
   #find all the hexagons containing var_index in csp_table
   #check if hexagon is a still a set with value discounting the dots
   assignment = list(assignment)
   assignment[var_index] = str(value)
   for hex in csp_table:
      if var_index in hex:
         if len(set([assignment[i] for i in hex if assignment[i] != "."])) != len([assignment[i] for i in hex if assignment[i] != "."]): return False
         #if len(set([assignment[i] for i in hex if assignment[i] != "."])) != 6 - hex.count("."): return False
 
   return True
 
def backtracking_search(input, csp_table): 
   return recursive_backtracking(input, csp_table)
 
def recursive_backtracking(assignment, csp_table):
   #assignment is the input
   #csp table is the list of hexagons by index
   """ your code goes here """
   if type(assignment) == list: assignment = "".join(assignment)
   if check_complete(assignment, csp_table): return assignment
   ind = select_unassigned_var(assignment,csp_table)
   assignment = list(assignment)
   for num in range(1,7):
      if isValid(num,ind,"".join(assignment),csp_table):
         assignment[ind] = str(num)
         res = recursive_backtracking(assignment,csp_table)
         if res != None: return res
         else: 
            assignment[ind] = "."
   return None
 
def display(solution):
   result = ""
   for i in range(len(solution)):
      if i == 0: result += "  "
      if i == 5: result += "\n"
      if i == 12: result += "\n"
      if i == 19: result += "\n  "
      result += solution[i] + " "
   return result
 
def main():
   csp_table = [[0, 1, 2, 6, 7, 8], [2, 3, 4, 8, 9, 10], [5, 6, 7, 12, 13, 14], [7, 8, 9, 14, 15, 16], [9, 10, 11, 16, 17, 18], [13, 14, 15, 19, 20, 21], [15, 16, 17, 21, 22, 23]] 
   solution = backtracking_search(input("24-char(. and 1-6) input: "), csp_table)
   if solution != None:
      print (display(solution))
      print ('\n'+ solution)
      print (check_complete(solution, csp_table))
   else: print ("It's not solvable.")
 
if __name__ == '__main__':
   main()
   
"""
Sample Output 1:
24-char(. and 1-6) input: ........................
  1 2 3 1 2 
1 4 5 6 4 5 1 
2 6 3 1 2 3 6 
  2 4 5 4 6 
 
123121456451263123624546
True
 
Sample Output 2:
24-char(. and 1-6) input: 6.....34...1.....2..4...
  6 1 2 1 3 
1 3 4 5 6 4 1 
5 6 2 1 3 2 5 
  3 4 5 4 6 
 
612131345641562132534546
True
"""