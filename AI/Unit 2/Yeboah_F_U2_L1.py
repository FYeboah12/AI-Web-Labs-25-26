# Name: Frances Yeboah
# Period: 5

from tkinter import *
from graphics import *
import random

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test 
   ''' your code goes here '''
   if len(assignment) == 0: return False
   for region in vars:
      if region not in assignment: return False
      if not isValid(assignment[region],region,assignment,vars,adjs): return False
   for reg in assignment:
      if reg == 'T': continue
      reg_color = assignment[reg]
      for neighbor in adjs[reg]:
         if neighbor in assignment and assignment[neighbor] == reg_color: return False
   return True

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   #LCV
   ''' your code goes here '''
   least_const = None
   max = 99999999
   for region in vars:
      if region in assignment:
         continue
      if len(vars[region]) < max:
         least_const = region
         max = len(vars[region])
   return least_const

   
def isValid(value, var, assignment, variables, adjs): #single state
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   ''' your code goes here '''
   if var == 'T': return True
   if len(assignment) == 0:
      return True
   if value in variables[var]:
      for neh in adjs[var]:
         if neh not in assignment: continue
         if assignment[neh] == value: return False
   return True

def backtracking_search(variables, adjs, shapes, frame): 
   return recursive_backtracking({}, variables, adjs, shapes, frame)

def recursive_backtracking(assignment, variables, adjs, shapes, frame):
   # Refer the pseudo code given in class.
   ''' your code goes here '''
   #val is color
   if check_complete(assignment,variables,adjs): return assignment
   var = select_unassigned_var(assignment,variables,adjs)
   for color_val in variables[var]:
      if isValid(color_val,var,assignment,variables,adjs):
         assignment[var] = color_val
         res = recursive_backtracking(assignment,variables,adjs,shapes,frame)
         if res != None: return res
         else: del assignment[var]
   return None

# return shapes as {region:[points], ...} form
def read_shape(filename):
   infile = open(filename)
   region, points, shapes = "", [], {}
   for line in infile.readlines():
      line = line.strip()
      if line.isalpha():
         if region != "": shapes[region] = points
         region, points = line, []
      else:
         x, y = line.split(" ")
         points.append(Point(int(x), 300-int(y)))
   shapes[region] = points
   return shapes

# fill the shape
def draw_shape(points, frame, color):
   shape = Polygon(points)
   shape.setFill(color)
   shape.setOutline("black")
   shape.draw(frame)
   space = [x for x in range(999999)] # give some pause
   
def main():
   regions, variables, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
   ''' your code goes here '''
   nodes_File = open("mcNodes.txt","r")
   edges_File = open("mcEdges.txt","r")
   for region in nodes_File.readlines():
      regions.append(region.strip())
   # Fill variables by using regions list -- no additional code for this part
   for r in regions: variables[r] = {'red', 'green', 'blue'}

   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.
   ''' your code goes here '''
   for edge_Line in edges_File.readlines():
      single_edge = edge_Line.split()
      if single_edge[0] not in adjacents:
         adjacents[single_edge[0]] = {single_edge[1]}
      if single_edge[1] not in adjacents:
         adjacents[single_edge[1]] = {single_edge[0]}
      if single_edge[0] in adjacents:
         adjacents[single_edge[0]].add(single_edge[1])
      if single_edge[0] in adjacents:
         adjacents[single_edge[1]].add(single_edge[0])
 
   # Set graphics -- no additional code for this part
   frame = GraphWin('Map', 300, 300)
   frame.setCoords(0, 0, 299, 299)
   shapes = read_shape("mcPoints.txt")
   for s, points in shapes.items():
      #print(s)
      draw_shape(points, frame, 'white')
  
   # solve the map coloring problem by using backtracking_search -- no additional code for this part  
   solution = backtracking_search(variables, adjacents, shapes, frame)
   print (solution)
   for s, points in shapes.items():
         draw_shape(points, frame, solution[s])
   mainloop()

if __name__ == '__main__':
   main()
   
''' Sample output:
{'WA': 'red', 'NT': 'green', 'SA': 'blue', 'Q': 'red', 'NSW': 'green', 'V': 'red', 'T': 'red'}
By using graphics functions, visualize the map.
'''