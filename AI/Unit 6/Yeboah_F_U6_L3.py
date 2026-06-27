import sys; args = sys.argv[1:]
circle = args[0]
#circle = "x*x+y*y<=1.396164020921283"
import math, random, time

# t_funct is symbol of transfer functions: 'T1', 'T2', 'T3', or 'T4'
# input is a list of input (summation) values of the current layer
# returns a list of output values of the current layer
def transfer(t_funct, input):
   if t_funct == 'T3': return [0 if x < -100 else 1 if x > 100  else 1 / (1 + math.e**-x) for x in input]
   elif t_funct == 'T4': return [-1+2/(1+math.e**-x) for x in input]
   elif t_funct == 'T2': return [x if x > 0 else 0 for x in input]
   else: return [x for x in input]

# returns a list of dot_product result. the len of the list == stage
# dot_product([x1, x2, x3], [w11, w21, w31, w12, w22, w32], 2) => [x1*w11 + x2*w21 + x3*w31, x1*w12, x2*w22, x3*w32] 
def dot_product(input, weights, stage):
   return [sum([input[x]*weights[x+s*len(input)] for x in range(len(input))]) for s in range(stage)]

# Complete the whole forward feeding for one input(training) set
# return updated x_vals and error of the one forward feeding
def ff(ts, xv, weights, t_funct):
   for stage_num in range(len(xv)-1):
      stage = xv[stage_num]
      xv[stage_num + 1] = dot_product(stage,weights[stage_num],len(xv[stage_num + 1]))
      if stage_num < len(xv) - 2:
         xv[stage_num + 1] = transfer(t_funct,xv[stage_num + 1])
      else:
         xv[stage_num + 1] = transfer('T1',xv[stage_num + 1])
         xv[stage_num + 1] = [max(-10.0, min(10.0, v)) for v in xv[stage_num + 1]]
      #err = sum([(ts[i-len(xv[-1])] - xv[-1][i])**2 for i in range(len(xv[-1]))]) / 2
      err = sum([(ts[i-len(xv[-1])] - xv[-1][i])**2 for i in range(len(xv[-1]))]) / 2
   return xv, err

# Complete the back propagation with one training set and corresponding x_vals and weights
# update E_vals (ev) and negative_grad, and then return those two lists
def bp(ts, xv, weights, ev, negative_grad):   
   ''' bp coding goes here '''
   ev[-1] = [(ts[i - len(xv[-1])] - xv[-1][i]) for i in range(len(xv[-1]))]
   for layer in range(len(ev)-1, 1, -1):
        n_prev = len(ev[layer-1])
        ev[layer-1] = [xv[layer-1][x] * (1 - xv[layer-1][x]) * sum(weights[layer-1][x + s * n_prev] * ev[layer][s] for s in range(len(ev[layer]))) for x in range(n_prev)]
   for layer in range(len(negative_grad)-1,-1,-1):
      current_error = []
      for e in ev[layer + 1]:
         for i in xv[layer]:
            current_error.append(i * e)
      negative_grad[layer] = current_error
   return ev, negative_grad

# update all weights and return the new weights
# Challenge: one input solution is possible
def update_weights(weights, negative_grad, alpha):

   ''' update weights (modify NN) code goes here '''
   for layer in range(len(weights)):
      weights[layer] = [alpha * negative_grad[layer][cur] + weights[layer][cur] for cur in range(len(weights[layer]))]

   return weights

def parse_input(input):
   #fix training set
   #sample operators: >= <= > <
   ops = ['>=','<=','>','<']
   ts = []
   end_sign_index = 9 if ops[0] in input or ops[1] in input else 8
   sign = input[7:end_sign_index]
   radius = float(input[end_sign_index:])
      #print(f"sign: {sign}, radius: {radius}")
      #find the closest sqrts
   sqrt = math.sqrt(radius)
   for i in range(250):
      x = random.uniform(-1.5,1.5)
      y = random.uniform(-1.5,1.5)
      pot_radius = x**2 + y**2
      in_or_out = None
      if sign == '>':
         in_or_out = 1 if pot_radius > radius else 0
      elif sign == '>=':
         in_or_out = 1 if pot_radius >= radius else 0
      elif sign == '<':
         in_or_out = 1 if pot_radius < radius else 0
      else:
         in_or_out = 1 if pot_radius <= radius else 0
      ts.append([x,y,in_or_out])
   ts += [[0,sqrt,1],[sqrt,0,1],[0,-sqrt,1],[-sqrt,0,1],[0,sqrt-0.01,1],[sqrt-0.01,0,1],[0,-sqrt+0.01,1],[-sqrt+0.01,0,1]]
   for j in range(150):
      theta = random.randint(0,360)
      x = radius * math.cos(theta)
      y = radius * math.sin(theta)
      ts.append([x,y,1])
   # ts.append([sqrt - 0.01,sqrt - 0.01])
   # ts.append([sqrt - 0.01,-sqrt + 0.01])
   # ts.append([-sqrt + 0.01,sqrt - 0.01])
   # ts.append([-sqrt + 0.01,-sqrt + 0.01])
   # #ts.append([]) s# should i add the sqrt boundary
   #    #print(f"sqrt of {radius} is: {round(sqrt,5)}\n")
   # for i in range(200):
   #    x = round(random.uniform(-1.5,1.5),3)
   #    y = round(random.uniform(-1.5,1.5),3)
   #    ts.append([x,y])
   #    #[-sqrt,sqrt] is in the circle
   #    # print(f"range is from [-{sqrt},{sqrt}]")
   #    # print(f"check if true: {x**2} + {y**2} = {round(x**2 + y**2,2)} {sign} {radius ** 2}")
   return ts

def main():
   
   t_funct = 'T3'
   training_set = parse_input(circle)
   #print(training_set)
   layer_counts = [3, 8, 8, 1, 1] #has to be 3 fix it

   def make_xvals():
      xv = []
      for temp in training_set:
         row = [list(temp[:2]) + [1.0]]
         for j in range(1, len(layer_counts)):
            row.append([0] * layer_counts[j])
         xv.append(row)
      return xv

   def make_weights():
      w = []
      for i in range(len(layer_counts)-2):
         w.append([round(random.uniform(-1,1),2) for _ in range(layer_counts[i] * layer_counts[i+1])])
      w.append([round(random.uniform(0.1,0.275),2) for _ in range(layer_counts[-2] * layer_counts[-1])])
      return w

   weights = [[round(random.uniform(-1.5, 1.5), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-2)]
   weights.append([round(random.uniform(-1.5, 1.5), 2) for i in range(layer_counts[-1])])
   x_vals = make_xvals()
   E_vals = [[[*node] for node in sample] for sample in x_vals]
   negative_grad = [w[:] for w in weights]
   errors = [10]*len(training_set)
   count = 1
   alpha = 0.4375
   best_err = 9999
   prev_err = 9999
   best_weights = None
   no_improve = 0
   deadline = time.time() + 97.5

   for k in range(len(training_set)):
      x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
   err = sum(errors)
   print(f"error: {err}")

   while best_err >= 0.01 and time.time() <= deadline:
      for k in range(len(training_set)):
         x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
         E_vals[k], negative_grad = bp(training_set[k], x_vals[k], weights, E_vals[k], negative_grad)
         weights = update_weights(weights, negative_grad, alpha)

      for m in range(len(training_set)):
         x_vals[m], errors[m] = ff(training_set[m], x_vals[m], weights, t_funct)
      err = sum(errors)
      print(f"new err: {err}, count: {count}")
      if err < best_err:
         best_err = err
         best_weights = [w[:] for w in weights]

      if abs(prev_err - err) < prev_err * 0.001:
         no_improve += 1
      else:
         no_improve = 0
      prev_err = err
      if no_improve >= 200:
         weights = make_weights()
         x_vals = make_xvals()
         E_vals = [[[*node] for node in sample] for sample in x_vals]
         negative_grad = [w[:] for w in weights]
         no_improve = 0
         prev_err = 9999

      count += 1

   if best_weights is not None:
      weights = best_weights

# at the end: > 0.5 return 1, < 0.5 return 0
   print(f"final error: {best_err}")
   print(f"Layer counts: {layer_counts}")
   print ("weights:")
   for w in weights:
      print([round(weight,5) for weight in w])
if __name__ == '__main__': main()

# Frances Yeboah, P5, 2027