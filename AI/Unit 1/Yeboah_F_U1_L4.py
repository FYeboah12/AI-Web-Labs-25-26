# Name: Frances Yeboah         Date: 9/10/25
import random, time, math

class HeapPriorityQueue():
    def __init__(self):
        self.queue = ["dummy"]
        self.current = 1

    def next(self):
        if self.current >= len(self.queue):
            self.current
            raise StopIteration
        out = self.queue[self.current]
        self.current += 1
        return out
    
    def __iter__(self):
        return self
    
    __next__ = next

    def isEmpty(self):
        return len(self.queue) == 1
    
    def swap(self,a,b):
        self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

    def remove(self,index):
        rem = self.queue[index]
        self.swap(index,len(self.queue)-1)
        self.queue.pop()
        self.heapDown(index,len(self.queue)-1)
        #self.heapUp(index)
        return rem
    
    def pop(self):
        # pop = self.queue.pop(1)
        # self.reheap()
        # return pop
        return self.remove(1)
    
    def push(self, value):
        self.queue.append(value)
        self.heapUp(len(self.queue)-1)
    
    def peek(self):
        return self.queue[1]
    
    def reheap(self):
        size = len(self.queue)//2
        for k in range(size,0,-1):
            self.heapDown(k,size)
    
    def heapDown(self,k,size): #fix this
        left = k*2
        right = k*2+1
        if left == size and self.queue[k] > self.queue[size]:
            self.swap(k,size)
        elif right <= size:
            min_child_index = k * 2 if self.queue[k*2] < self.queue[k*2+1] else k*2+1
            if self.queue[k] > self.queue[min_child_index]:
                self.swap(k,min_child_index)
            self.heapDown(min_child_index, size)
    # def heapDown(self, k, size):
    #     while 2 * k < size:
    #         left = 2 * k
    #         right = left + 1
    #         smallest = left

    #         if right < size and self.queue[right] < self.queue[left]:
    #             smallest = right

    #         if self.queue[k] > self.queue[smallest]:
    #             self.swap(k, smallest)
    #             k = smallest
    #         else:
    #             break

    def heapUp(self,k):
        parent = k // 2
        while parent != 0 and self.queue[parent] > self.queue[k]:
            self.swap(k,parent)
            k = parent
            parent = k // 2

def inversion_count(new_state, width = 4, N = 4):
   ''' 
   Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
   ''' 

   #N is height (4x4), (3x3)
   # Your code goes here
   inv_count = 0
   NisEven = N % 2 == 0
   blank = new_state.index("_")
   row = blank // width
   if NisEven:
       for i in range(len(new_state)):
           for j in range(i + 1, len(new_state)):
               if new_state[i] != "_" and new_state[j] != "_" and new_state[i] > new_state[j]:
                   inv_count += 1
       return (inv_count % 2 == 0 and row % 2 == 0) or (inv_count % 2 == 1 and row % 2 == 1)
   else:
        for i in range(len(new_state)):
           for j in range(i+1,len(new_state)):
               if new_state[i] != "_" and new_state[j] != "_" and new_state[i] > new_state[j]:
                   inv_count += 1
        return inv_count % 2 == 0

def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   f1 = inversion_count("21345678_", 3, 3)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   print(t1,t2,f1,f2)
   return t1 and t2 and not (f1 or f2)




def getInitialState(sample, size):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   while not inversion_count(new_state, size, size): 
      random.shuffle(sample_list)
      new_state = ''.join(sample_list)
   return new_state
   
def swap(n, i, j):
   # Your code goes here
    sl = list(n)
    a = sl[i]
    sl[i] = sl[j]
    sl[j] = a
    return "".join(sl)
      
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state, size=4):
   children = []
   blank = state.find('_')
   '''your code goes here'''
   row = blank // size
   col = blank % size
   for r,c in [(row, col + 1),(row, col - 1),(row + 1, col),(row - 1, col)]:
      if 0 <= r < size and 0 <= c < size:
         ind = r * size + c
         children.append(swap(state,blank,ind))
   return children

def display_path(path_list, size):
   for n in range(size):
      for path in path_list:
         print (path[n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

''' You can make multiple heuristic functions '''
def dist_heuristic(state, goal = "_123456789ABCDEF", size=4):
   # Your code goes here
   # blank = state.index("_")
   # row = blank // size
   # col = blank  % size
   # return row + col
   #num of misplaced tiles
   misplaced = 0
   for i in range(len(state)):
       if state[i] != goal[i]:
           misplaced += 1
   return misplaced


def check_heuristic():
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   #print(a, b)
   return (a < b) 

def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   #(cost, currentLetter, path)
   frontier = HeapPriorityQueue()
   if start == goal: return []
   #path = set(start)
   explored = {start: 0} 
   family = {}
   frontier.push((heuristic(start), start))
   # Your code goes here
   while len(frontier.queue) > 1:
       current = frontier.pop()[1]
       #current_cost = heuristic(current)
       current_cost = explored[current]
       if current == goal:
           path = [goal]
           while current in family:
               current = family[current]
               path.append(current)
           return path[::-1]
           #return explored
       for child in generate_children(current):
           child_cost = current_cost + 1
           if child not in explored or explored[child] > child_cost:
               explored[child] = child_cost
               frontier.push((child_cost + heuristic(child),child))
               family[child] = current
               
   return None

def main():
    # A star
   print ("Inversion works?:", check_inversion())
   print ("Heuristic works?:", check_heuristic())
   #initial_state = getInitialState("_123456789ABCDEF", 4)
   initial_state = input("Type initial state: ")
   if inversion_count(initial_state):
      cur_time = time.time()
      path = (a_star(initial_state))
      if path != None: display_path(path, 4)
      else: print ("No Path Found.")
      print ("Duration: ", (time.time() - cur_time))
   else: print ("{} did not pass inversion test.".format(initial_state))
   
if __name__ == '__main__':
   main()


''' Sample output 1

Inversion works?: True
Heuristic works?: True
Type initial state: 152349678_ABCDEF
1523    1523    1_23    _123    
4967    4_67    4567    4567    
8_AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 4
Duration:  0.0


Sample output 2

Inversion works?: True
Heuristic works?: True
Type initial state: 2_63514B897ACDEF
2_63    _263    5263    5263    5263    5263    5263    5263    5263    52_3    5_23    _523    1523    1523    1_23    _123    
514B    514B    _14B    1_4B    14_B    147B    147B    147_    14_7    1467    1467    1467    _467    4_67    4567    4567    
897A    897A    897A    897A    897A    89_A    89A_    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 16
Duration:  0.005014657974243164


Sample output 3

Inversion works?: True
Heuristic works?: True
Type initial state: 8936C_24A71FDB5E
8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 37
Duration:  0.27825474739074707


Sample output 4

Inversion works?: True
Heuristic works?: True
Type initial state: 8293AC4671FEDB5_
8293    8293    8293    8293    8293    8293    8293    8293    82_3    8_23    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
AC46    AC46    AC46    AC46    AC46    _C46    C_46    C4_6    C496    C496    C_96    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
71FE    71F_    71_F    7_1F    _71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5_    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 39
Duration:  0.7709157466888428

'''

