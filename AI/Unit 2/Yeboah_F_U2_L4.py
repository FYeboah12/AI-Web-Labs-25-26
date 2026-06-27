import sys; args = sys.argv[1:]
puzzles = open(args[0]).read().splitlines()
import time

STATS = {}
def noteStat(phrase):
    STATS[phrase] = STATS.get(phrase,0)+1

def findBestSym(assignment,variables): #actually follow paper (rememer what you said {*"123456789"})
   #for each const set
   #for each unset symbol
   #if the number of available positions in the const set is less than the set of choices
   #update
   best = -1
   for const in LIST_OF_CONST_SETS: #list
      for i in const:
         if assignment[i] != ".":
            continue #index of an unset symbol
         avail_pos = [x for x in const if assignment[x] == "."]
         if len(avail_pos) < len(variables[i]):
            for val in avail_pos:
               valid, variables = update_variables(val,i,assignment,variables,csp)
               if valid: best = i
               avail = {1,2,3,4,5,6,7,8,9} - set([int(assignment[x]) for x in NEIGHBORS[best] if assignment[x] != "."]) #possible values
            return best, avail
            # for val in avail_pos:
            #    valid, variables = update_variables(val,i,assignment,variables,csp)
            #    if valid: best = i
         #avail = {1,2,3,4,5,6,7,8,9} - set([int(assignment[x]) for x in NEIGHBORS[i] if assignment[x] != "."]) #possible values
         # if len(avail) < len(variables[i]):
         #    for val in avail:
         #       valid, variables = update_variables(val,i,assignment,variables,csp)
         #       if valid: best = i
   #update variables
   avail = {1,2,3,4,5,6,7,8,9} - set([int(assignment[x]) for x in NEIGHBORS[best] if assignment[x] != "."]) #possible values
   return best, avail #sym, pos

def check_invalid(ind,assignment):
   #check if val in neighbors
   # for cs in LIST_OF_CONST_SETS:
   #    filled_in = [assignment[i] for i in cs if assignment[i] != "."]
   #    if len(set(filled_in)) < len(filled_in):
   #       return True
   # return False
   for cs in POS_TO_CONST[ind]:
      filled_in = [assignment[i] for i in cs if assignment[i] != "."]
      if len(set(filled_in)) < len(filled_in):
         return True
   return False


def setGlobals():
   global N,W,LIST_OF_CONST_SETS,POS_TO_CONST,NEIGHBORS,ONE_THRU_NINE,csp
   csp = sudoku_csp()
   N = 9
   W = 9
   ONE_THRU_NINE = {1,2,3,4,5,6,7,8,9}
   LIST_OF_CONST_SETS = [set(x) for x in csp] #rows, cols, sub blocks (lookup table)
   POS_TO_CONST = {pos: [cc for cc in LIST_OF_CONST_SETS if pos in cc] for pos in range(81)} #position to constraint set (rows, cols, subblocks its in) 
   NEIGHBORS = {k:set() for k in range(N*N)}
   for t in csp:
      for p in t:
         NEIGHBORS[p] = NEIGHBORS[p] | set(t) #union 
   NEIGHBORS = {k:NEIGHBORS[k] - {k} for k in NEIGHBORS} #set of all numbers within r,c,s



def checksum(puzzle):
    return sum([ord(c) for c in puzzle]) - len(puzzle)*ord(min(puzzle)) #ord returns ascii value of character
'''sum the ascii value of each symbol in
your puzzle and subtract (the length of the puzzle) * (the ascii value of the min symbol in
your puzzle). Until your code is rock solid, do this as a simple way of double checking
your Sudoku solution correctness.'''
 
# def check_complete(assignment, csp_table):
#    if assignment.find('.') != -1: return False
#    for sudoku in csp_table:
#       if len(set([assignment[i] for i in sudoku])) != 9: return False
#    return True
   
def select_unassigned_var(assignment, variables, csp_table):
    for i in range(81):
       if assignment[i] != ".":
            continue
       cb = set([int(assignment[x]) for x in NEIGHBORS[i] if assignment[x] != "."])
       choices = {1,2,3,4,5,6,7,8,9} - cb
       if len(choices) <= 1:
         return i,choices 
    return findBestSym(assignment,variables)
    #findBestSym(assignment,variables)
   #  #mrv, optimize
   # #  #options = {}
   # #  most_count = 0
   # #  most_constrained_index = -1
   # #  for i in range(81):
   # #     if assignment[i] != ".":
   # #          continue
   # #     cannot_be = set([assignment[x] for x in NEIGHBORS[i] if x != "."])
   # #     if len(cannot_be) >= most_count:
   # #       #options[i]  = len(cannot_be)
   # #       most_count = len(cannot_be)
   # #       most_constrained_index = i
   # #     #call findBestSym with > 1 choice
   # # #  biggest = sorted(options, key=options.get, reverse=True)[0] 
   # # #  callFBS = [k for k, v in options.items() if v == options[biggest]]
   # # #  if len(callFBS) > 1: findBestSym(callFBS,assignment,variables,csp_table)  
   # #  #findBestSym(0,assignment,variables,csp_table)
   # #  return most_constrained_index
   #  options = []
   #  #most_count = 999999
   #  #most_constrained_index = -1
   #  for i in range(81):
   #     if assignment[i] != ".":
   #          continue
   #     cb = set([int(assignment[x]) for x in NEIGHBORS[i] if assignment[x] != "."]) #filled in values
   #     choices = {1,2,3,4,5,6,7,8,9} - cb #available values
   #     if len(choices) <= 1:
   #       return i,choices
   #     options.append((i,choices))
   #     #call findBestSym with > 1 choice
   #  return min(options)[0]
   #  #findBestSym(assignment,variables,csp_table)
   #  #return most_constrained_index
 
def isValid(value, var_index, assignment):
   filledValues = [assignment[x] for x in NEIGHBORS[var_index] if assignment[x] != "."]
   return str(value) not in filledValues
   # for table in csp_table:
   #    if var_index in table:
   #       for i in table:
   #          if assignment[i] == value: return False
   # for vi, vals in variables.items():
   #    if len(vals) == 0: return False
   # return True
 
# def ordered_domain(var_index, assignment, variables, csp_table):
#    temp = {k:0 for k in variables[var_index]}
#    for a in assignment:
#       if a in temp: temp[a]+1
#    temp2 = sorted([(c,value) for value, c in temp.item()], reverse=True)
#    return [val for c, val in temp2]

def update_variables(value, var_index, assignment, variables, csp_table): #if value works
   #check if length is 0, return false
   temp = {k: {s for s in v} for k,v in variables.items()}
   consts = POS_TO_CONST[var_index]
   for c in consts:
      for i in c:
         if i != var_index:
            temp[i] -= {value}
            if len(temp[i]) == 0:
               return False, temp
   return True, temp
 
def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)
 
def recursive_backtracking(assignment, variables, csp_table):
   if type(assignment) == list: assignment = "".join(assignment)
   if assignment.find(".") == -1: return assignment #isSolved
   ind,pos = select_unassigned_var(assignment,variables,csp_table) 
   if ind != -1:
      if check_invalid(ind,assignment): return ""
   assignment = list(assignment)
   if ind != -1:
      for num in pos: #best sym
               noteStat(f"rb:{num}")
            # if isValid(num,ind,"".join(assignment),variables,csp_table):
            #    noteStat("successful isValid call")
               assignment[ind] = str(num)
               #valid, variables = update_variables(num,ind,assignment,variables,csp_table)
               res = recursive_backtracking(assignment,variables,csp_table)
               if res != None: return res
               else: 
                  assignment[ind] = "."
                  #variables = update_variables(num,ind,assignment,variables,csp_table)
   return None
 
 
def display(solution):
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
   magic_num = 9   
   return [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80],[x for x in range(magic_num)],[x for x in range(magic_num, magic_num * 2)],[x for x in range(magic_num * 2, magic_num * 3)],[x for x in range(magic_num * 3, magic_num * 4)],[x for x in range(magic_num * 4, magic_num * 5)],[x for x in range(magic_num * 5, magic_num * 6)],[x for x in range(magic_num * 6, magic_num * 7)],[x for x in range(magic_num * 7, magic_num * 8)],[x for x in range(magic_num * 8, magic_num * 9)],[x for x in range(0,81,magic_num)],[x for x in range(1,81,magic_num)],[x for x in range(2,81,magic_num)],[x for x in range(3,81,magic_num)],[x for x in range(4,81,magic_num)],[x for x in range(5,81,magic_num)],[x for x in range(6,81,magic_num)],[x for x in range(7,81,magic_num)],[x for x in range(8,81,magic_num)]]
 
def initial_variables(puzzle, csp_table):
   avail_nums = [n for n in range(1,10)]
   vars = {}
   for i in range(len(puzzle)):
      vars[i] = avail_nums
   return vars
   
def main():
   setGlobals()

   # puzzle = input("Type a 81-char string: ") 
   # while len(puzzle) != 81:
   #    print ("Invalid puzzle")
   #    puzzle = input("Type a 81-char string: ")
   # csp_table = sudoku_csp()
   # variables = initial_variables(puzzle, csp_table)
   # print ("Initial:\n" + display(puzzle))
   # solution = backtracking_search(puzzle, variables, csp_table)
   # if solution != None: print ("solution\n" + display(solution))
   # else: print ("No solution found.\n")   

   csp = sudoku_csp()
   start = time.time()
   for l, p in enumerate(puzzles):
         if time.time()-start >= 60: break
         #if l == 50:  break
         l, p = l + 1, p.strip()
         print("{}: {}".format(l,p))
         vars = initial_variables(p,csp)
         solution = backtracking_search(p,vars,csp)
         if solution == None: print("No solution"); break
         print("{}{} {}".format(" "*(len(str(l))+2),solution,checksum(solution)))
   print("Duration",(time.time()-start), "seconds")
   
if __name__ == '__main__': main()
 
# Frances Yeboah, P5, 2027