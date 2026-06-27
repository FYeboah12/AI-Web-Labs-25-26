# Name: Frances Yeboah
# Date: 10/3/25
 
def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for sudoku in csp_table:
      if len(set([assignment[i] for i in sudoku])) != 9: return False
   return True
   
def select_unassigned_var(assignment, variables, csp_table):
    most_count = -1
    most_constrained_index = -1
    for i in range(len(assignment)):
        if assignment[i] != ".":
            continue
        count = 0
        for group in csp_table:
            if i in group:
                count += 1
        if count > most_count:
            most_count = count
            most_constrained_index = i
 
    return most_constrained_index
 
def isValid(value, var_index, assignment, variables, csp_table):
   assignment = list(assignment)
   assignment[var_index] = str(value)
   for hex in csp_table:
      if var_index in hex:
         if len(set([assignment[i] for i in hex if assignment[i] != "."])) != len([assignment[i] for i in hex if assignment[i] != "."]): return False
         #if len(set([assignment[i] for i in hex if assignment[i] != "."])) != 6 - hex.count("."): return False
 
   return True
 
def ordered_domain(var_index, assignment, variables, csp_table):
   return variables[var_index]
   #look in variables for var_index with lcv
   # ordered = []
   # available_numbers = variables[var_index]
   # count = 0
   # least_count = 0
   # least_const_index = -1
   # for i in range(len(assignment)):
   #    for r in range(len(csp_table)):
   #       for c in range(len(csp_table[0])):
   #             if csp_table[r][c] == i and assignment[i] == ".":
   #                count += 1
   #    if count > least_count and count > 0: 
   #       least_count = count
   #       least_const_index = i
   #    count = 0
   # return ordered #indices in order of lcv
 
def update_variables(value, var_index, assignment, variables, csp_table):
   updated = [x for x in variables[var_index] if x != value]
   variables[var_index] = updated
   
   # index_of_value = updated.index(value)
   # del updated[index_of_value]
   #variables[var_index] = updated
   return variables
 
def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)
 
def recursive_backtracking(assignment, variables, csp_table):
   if type(assignment) == list: assignment = "".join(assignment)
   #print(display(assignment), "\n")
   if check_complete(assignment, csp_table): return assignment
   ind = select_unassigned_var(assignment,variables,csp_table)
   assignment = list(assignment)
   for num in variables[ind]:
      if isValid(num,ind,"".join(assignment),variables,csp_table):
         assignment[ind] = str(num)
         res = recursive_backtracking(assignment,variables,csp_table)
         if res != None: return res
         else: 
            assignment[ind] = "."
            
      #variables = update_variables(num,ind,assignment,variables,csp_table)
   return None
 
 
def display(solution):
   #solution is the 81 char
   #big newlines: 26 and 53
   #tabs: 2,11,20,5,14,23,29,38,47,32,41,50,56,65,74,59,68,77
   result = ""
   for i in range(len(solution)):
        result += solution[i] + " "
        if i == 26 or i == 53:
           result += "\n\n"
        if i in [8,17,35,44,62,71]:
            result += "\n"
        if i in [2,11,20,5,14,23,29,38,47,32,41,50,56,65,74,59,68,77]:
           result += "\t"
   return result
 
def sudoku_csp():
   #27: 9 for square, 9 for row, 9 for column
   magic_num = 9   
   return [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80],[x for x in range(magic_num)],[x for x in range(magic_num, magic_num * 2)],[x for x in range(magic_num * 2, magic_num * 3)],[x for x in range(magic_num * 3, magic_num * 4)],[x for x in range(magic_num * 4, magic_num * 5)],[x for x in range(magic_num * 5, magic_num * 6)],[x for x in range(magic_num * 6, magic_num * 7)],[x for x in range(magic_num * 7, magic_num * 8)],[x for x in range(magic_num * 8, magic_num * 9)],[x for x in range(0,81,magic_num)],[x for x in range(1,81,magic_num)],[x for x in range(2,81,magic_num)],[x for x in range(3,81,magic_num)],[x for x in range(4,81,magic_num)],[x for x in range(5,81,magic_num)],[x for x in range(6,81,magic_num)],[x for x in range(7,81,magic_num)],[x for x in range(8,81,magic_num)]]
   #square rule- #hard code for now
   # square = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
   #row rule- 
   # row = [[x for x in range(magic_num)],[x for x in range(magic_num, magic_num * 2)],[x for x in range(magic_num * 2, magic_num * 3)],[x for x in range(magic_num * 3, magic_num * 4)],[x for x in range(magic_num * 4, magic_num * 5)],[x for x in range(magic_num * 5, magic_num * 6)],[x for x in range(magic_num * 6, magic_num * 7)],[x for x in range(magic_num * 7, magic_num * 8)],[x for x in range(magic_num * 8, magic_num * 9)]]
   #col rule-
   # col = [[x for x in range(0,81,magic_num)],[x for x in range(1,81,magic_num)],[x for x in range(2,81,magic_num)],[x for x in range(3,81,magic_num)],[x for x in range(4,81,magic_num)],[x for x in range(5,81,magic_num)],[x for x in range(6,81,magic_num)],[x for x in range(7,81,magic_num)],[x for x in range(8,81,magic_num)]]
   #print(row, "\n\n\n\n", col)
   #return [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
 
def initial_variables(puzzle, csp_table):
   avail_nums = [n for n in range(1,10)]
   vars = {}
   for i in range(len(puzzle)):
      vars[i] = avail_nums
   return vars
   
def main():
   puzzle = input("Type a 81-char string:") 
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   variables = initial_variables(puzzle, csp_table)
   print ("Initial:\n" + display(puzzle))
   solution = backtracking_search(puzzle, variables, csp_table)
   if solution != None: print ("solution\n" + display(solution))
   else: print ("No solution found.\n")
   
if __name__ == '__main__': main()
 
# Frances Yeboah, P5, 2027