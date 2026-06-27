import sys; args = sys.argv[1:]
#ints = open("x_gate.txt")
ints = open(args[0])
import math, random, time
'''DO TRY EXCEPT TO PREVENT OVERFLOW ERROR: RETURN 1 OR 0 (there are too many decimal places)'''


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
   # n_out = len(xv[-1])
   # ev[-1] = [(ts[-(n_out - i)] - xv[-1][i]) * xv[-1][i] * (1 - xv[-1][i]) for i in range(n_out)]
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

#    #print("ev:",ev,"\nng:",negative_grad)
#    #ev[-1] = [ts[-1] - xv[-1][0]] #target - y
#    #ev[-1] = [(ts[-1] - xv[-1][0]) * xv[-1][0] * (1- xv[-1][0])] #wrong
#    ev[-1] = [(ts[i - len(xv[-1])] - xv[-1][i]) * xv[-1][i] * (1 - xv[-1][i]) for i in range(len(xv[-1]))]
#    for layer in range(len(ev)-1,1,-1):
#       ev[layer - 1] = [weights[layer - 1][x] * xv[layer - 1][x] * (1-xv[layer - 1][x]) * ev[layer][0] for x in range(len(ev[layer-1]))]
#    for layer in range(len(negative_grad)-1,-1,-1): #going backwards
#       current_error = []
#       for e in ev[layer + 1]:
#          for i in xv[layer]:
#             current_error.append(i * e)
#       negative_grad[layer] = current_error
#    #print("ev:",ev,"\nng:",negative_grad,"\n\n")
#   #ev is error value  
#    return ev, negative_grad

# update all weights and return the new weights
# Challenge: one line solution is possible
def update_weights(weights, negative_grad, alpha):

   ''' update weights (modify NN) code goes here '''
   for layer in range(len(weights)):
      weights[layer] = [alpha * negative_grad[layer][cur] + weights[layer][cur] for cur in range(len(weights[layer]))]

   return weights

def parse_input(input):
   #each line is its own training set: ff for each line => list of lists
   ts = []
   n_inputs = None
   line = input.readline()
   while line:
      if not line.strip():
         line = input.readline()
         continue
      nums = line.split()
      if "=>" in nums:
         arrow = nums.index("=>")
         if n_inputs is None:
            n_inputs = arrow
         del nums[arrow]
      nums = [float(num) for num in nums]
      ts.append(nums)
      line = input.readline()
   return ts, n_inputs
   # while line:
   #      nums = line.split()
   #      del nums[2]
   #      nums = [float(num) for num in nums]
   #      ts.append(nums)
   #      line = input.readline()
   #return ts

def main():
   
   t_funct = 'T3'
   training_set, n_inputs = parse_input(ints)
   layer_counts = [n_inputs + 1, 2, 1, 1]
   
   def make_xvals():
      xv = []
      for temp in training_set:
         row = [list(temp[:n_inputs]) + [1.0]]
         for j in range(1, len(layer_counts)):
            row.append([0] * layer_counts[j])
         xv.append(row)
      return xv

   def make_weights():
      w = []
      for i in range(len(layer_counts)-2):
         w.append([round(random.uniform(-1,1),2) for _ in range(layer_counts[i] * layer_counts[i+1])])
      w.append([round(random.uniform(0.1,1),2) for _ in range(layer_counts[-2] * layer_counts[-1])])
      return w

   weights = make_weights()
   x_vals = make_xvals()
   E_vals = [[[*node] for node in sample] for sample in x_vals]
   negative_grad = [w[:] for w in weights]
   errors = [10]*len(training_set)
   count = 1
   alpha = 1.5
   best_err = 9999
   prev_err = 9999
   best_weights = None
   no_improve = 0
   deadline = time.time() + 29.5

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
      '''if count % 3000 == 0:
         weights = make_weights()
         x_vals = make_xvals()
         E_vals = [[[*node] for node in sample] for sample in x_vals]
         negative_grad = [w[:] for w in weights]
         

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
      #print(best_err)
      count += 1

   if best_weights is not None:
      weights = best_weights'''

   # print(f"final error: {err}\n")    
   # layer_counts = [str(i) for i in layer_counts] 
   # output_lines = [f"Layer counts {' '.join(layer_counts)}"] 
   # for w_layer in weights: 
   #    output_lines.append(" ".join([str(round(w,5)) for w in w_layer])) 
   # print("\n".join(output_lines)) 


   # layer_counts = [str(i) for i in layer_counts] 
   # output_lines = [f"Layer counts {' '.join(layer_counts)}"] 
   # for w_layer in weights: 
   #    output_lines.append(" ".join([str(round(w,5)) for w in w_layer])) 
   # print("\n".join(output_lines)) 






   # t_funct = 'T3' # we default the transfer(activation) function as 1 / (1 + math.e**(-x))
   # ''' work on training_set and layer_count '''
   # training_set, n_inputs = parse_input(ints)  # list of lists
   # n_outputs = len(training_set[0]) - n_inputs
   # #print (training_set) #[[1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [-1.0, -1.0, 1.0], [0.0, 0.0, 0.0]]
   # layer_counts = [n_inputs + 1, 2, 1, n_outputs] # set the number of layers: (# of input + 1), (# of output + 1), # of output, # of output
   # #layer_counts = [len(training_set[0]),4,1]
   # #print ('layer counts', layer_counts) # This is the first output. [3, 2, 1, 1] with teh given x_gate.txt
   #  #might need to fix layer counts >_<
   # ''' build NN: x nodes and weights '''
   # x_vals = [[temp[0:len(temp)-1]] for temp in training_set] # x_vals starts with first input values
   # #print (x_vals) # [[[1.0, -1.0]], [[-1.0, 1.0]], [[1.0, 1.0]], [[-1.0, -1.0]], [[0.0, 0.0]]]
   # # make the x value structure of the NN by putting bias and initial value 0s.
   # for i in range(len(training_set)):
   #    for j in range(len(layer_counts)):
   #       if j == 0: x_vals[i][j].append(1.0)
   #       else: x_vals[i].append([0 for temp in range(layer_counts[j])])
   # #print ("xvals",x_vals) # [[[1.0, -1.0, 1.0], [0, 0], [0], [0]], [[-1.0, 1.0, 1.0], [0, 0], [0], [0]], ...

   # # by using the layer counts, set initial weights [3, 2, 1, 1] => 3*2 + 2*1 + 1*1: Total 6, 2, and 1 weights are needed
   # weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-2)]
   # weights.append([round(random.uniform(-2.0, 2.0), 2) for i in range(layer_counts[-1])])
   # #weights = [[1.35, -1.34, -1.66, -0.55, -0.9, -0.58, -1.0, 1.78], [-1.08, -0.7], [-0.6]]   #Example 2
   # # print (weights)    #[[2.0274715389784507e-05, -3.9375970265443985, 2.4827119599531016, 0.00014994269071843774, -3.6634876683142332, -1.9655046461270405]
   #                      #[-3.7349985848630634, 3.5846029322774617]
   #                      #[2.98900741942973]]
   # #weights = [[0.92,-1.66,-1.42,-1.15,0.46,1.41],[-1.32,-0.82],[-0.54]] #test weights!

   # # build the structure of BP NN: E nodes and negative_gradients 
   # E_vals = [[[*i] for i in j] for j in x_vals]  #copy elements from x_vals, E_vals has the same structures with x_vals
   # negative_grad = [[*i] for i in weights]  #copy elements from weights, negative gradients has the same structures with weights
   # errors = [10]*len(training_set)  # Whenever FF is done once, error will be updated. Start with 10 (a big num)
   # count = 1  # count how many times you trained the network, this can be used for index calc or for decision making of 'restart'
   # alpha = 1.5 #og 0.3
   # # best_err = float('inf')
   # # best_weights = None

   # # calculate the initail error sum. After each forward feeding (# of training sets), calculate the error and store at error list
   # for k in range(len(training_set)):
   #    x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
   #    #bp(training_set[k], x_vals[k], weights, E_vals[k],negative_grad[k])
   #    #sum??
   #    #bp
   #    #modify weights
   # err = sum(errors)
   # print("error:", err)
   # while err > 0.01 and count <= 10000:
   #    for k in range(len(training_set)):
   #       if count >= 1000:
   #          alpha = 1.025
   #       if count >= 2500:
   #          alpha = 0.3
   #       if count >= 5000: #restart?
   #          alpha = 0.075
   #       if count >= 7500:
   #          alpha = 0.05
   #       if count >= 10000:
   #          alpha = 0.03
   #       if count >= 12500:
   #          alpha = 0.01
   #       if count >= 25000:
   #          alpha = 0.001
   #       if count == 1250:
   #          weights = [[round(random.uniform(-1, 1), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-2)]
   #          weights.append([round(random.uniform(-1, 1), 2) for i in range(layer_counts[-1])])
   #       x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
   #       E_vals[k], negative_grad = bp(training_set[k], x_vals[k], weights, E_vals[k],negative_grad)
   #       weights = update_weights(weights,negative_grad,alpha)
   #       for l in range(len(training_set)):
   #          x_vals[l], errors[l] = ff(training_set[l], x_vals[l], weights, t_funct)
   #       err = sum(errors)
   #       #print(f"new err: {err}, count: {count}")
   #       count += 1


   # print(f"final error: {err}\n")   
   # layer_counts = [str(i) for i in layer_counts]
   # output_lines = [f"Layer counts {' '.join(layer_counts)}"]
   # for w_layer in weights:
   #    output_lines.append(" ".join([str(round(w,5)) for w in w_layer]))
   # print("\n".join(output_lines))

   ''' 
   while err is too big, reset all weights as random values and re-calculate the error sum.
   
   '''

   ''' 
   while err does not reach to the goal and count is not too big,
      update x_vals and errors by calling ff()
      whenever all training sets are forward fed, 
         check error sum and change alpha or reset weights if it's needed
      update E_vals and negative_grad by calling bp()
      update weights
      count++
   '''

   
      # while err > 0.01 and count <= 10000:
   #    if count != 1:
   #       for k in range(len(training_set)):
   #          x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
   #       err = sum(errors)
   #       print(f"new err: {err}, count: {count}")
   #    if err > 0.01:
   #       for k in range(len(training_set)):
   #             E_vals[k], negative_grad = bp(training_set[k], x_vals[k], weights, E_vals[k],negative_grad)
   #             weights = update_weights(weights,negative_grad,alpha)
   #       count += 1
   # print final weights of the working NN
   print(f"final error: {best_err}")
   print(f"Layer counts: {layer_counts}")
   #print(layer_counts)
   print ("weights:")
   for w in weights:
      print([round(weight,5) for weight in w])

   #for w in weights: print (w)
if __name__ == '__main__': main()

# Frances Yeboah, P5, 2027