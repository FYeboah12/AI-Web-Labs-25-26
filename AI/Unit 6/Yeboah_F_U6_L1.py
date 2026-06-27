import sys; args = sys.argv[1:]
file = open(args[0])
import math

def transfer(t_funct, input):   
   if t_funct == "T1": #linear
     return input
   elif t_funct == "T2": #ramp
      return input if input > 0 else 0
   elif t_funct == "T3": #logistic
      return (1/(1 + (math.exp(-input))))
   else: #sigmoid
      return -1 + (2/(1 + math.exp(-input)))

def dot_product(input, weights, stage):
   dp = []
   for i in range(len(stage)):
      dp.append(stage[i] * weights[i])
   return dp
   

def evaluate(file, input_vals, t_funct): #file is the weights, input_vals are the actual input vals
   #plan: split by the number of input vals (list)
   #read lines
   done = False
   layers = [] #contains the weights
   stages = []
   num_stages = len(input_vals)
   weights = file.readline()
   while weights:
      layers.append(weights.split())
      weights = file.readline()
   #split within the layer, dot product, save to list, sum(list), transfer function, repeat
   for index, layer in enumerate(layers):
      layer = [float(x) for x in layer]
      for i in range(0,len(layer),num_stages):
         stages.append(layer[i:i+num_stages]) #[[],[],[]]
      for i in range(len(stages)):
            stages[i] = dot_product(0,stages[i],input_vals)
            if index != len(layers) - 1:
               stages[i] = sum(stages[i])
               stages[i] = transfer(t_funct,stages[i])
            else:
               return stages[0]
      num_stages = len(stages)
      input_vals = stages
      stages = []
      
      #Make it stop before the last weight (don't do transfer again)
   
   return ""
     
def main():
   #weightFile.txt TransferFunctionSpec inputs ...
   inputs, t_funct, transfer_found = [], 'T1', False
   for arg in args[1:]:
      if not transfer_found:
         t_funct, transfer_found = arg, True
      else:
         inputs.append(float(arg))
   li =(evaluate(file, inputs, t_funct)) #ff
   for x in li:
      print (x, end=' ') # final outputs
if __name__ == '__main__': main()

# Frances Yeboah, P5, 2027