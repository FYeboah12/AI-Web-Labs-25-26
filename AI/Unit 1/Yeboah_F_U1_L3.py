import random


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
        #  self.swap(1,len(self.queue)-1)
        #  pop = self.queue.pop()
        #  self.reheap()
        #  return pop
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

    def heapUp(self,k):
        parent = k // 2
        while parent != 0 and self.queue[parent] > self.queue[k]:
            self.swap(k,parent)
            k = parent
            parent = k // 2

    # This method is for testing. Do not change it.
def isHeap(heap, k):
   left, right = 2*k, 2*k+1
   if left == len(heap): return True
   elif len(heap) == right and heap[k] > heap[left]: return False
   elif right < len(heap): 
      if (heap[k] > heap[left] or heap[k] > heap[right]): return False
      else: return isHeap(heap, left) and isHeap(heap, right)
   return True
    
# # This method is for testing. Do not change it.
def main():
        
   pq = HeapPriorityQueue()    # create a HeapPriorityQueue object
   
   print ("Check if dummy 0 is still dummy:", pq.queue[0])
   
   # assign random integers into the pq
   for i in range(20): #20
      t = random.randint(10, 99)
      print (t, end=" ")
      pq.push(t)
#    pq.push(69)
#    pq.push(83)
#    pq.push(44)
#    pq.push(18)
#    pq.push(26)
#    pq.push(21)
#    pq.push(88)
#    pq.push(26)
#    pq.push(39)
#    pq.push(13)
#    pq.push(68)
#    pq.push(35)
#    pq.push(44)
#    pq.push(97)
#    pq.push(71)
#    pq.push(33)
#    pq.push(30)
#    pq.push(34)
#    pq.push(74)
#    pq.push(45)
   print ()
   # print the pq which is a min-heap
   for x in pq:
      print (x, end=" ")
   print()
   
   # remove test
   print ("Index 4 is removed:", pq.remove(4))
   
   # check if pq is a min-heap
   for x in pq:
      print (x, end=" ")
   print("\nIs a min-heap?", isHeap(pq.queue, 1))
   
   temp = []
   while not pq.isEmpty():
      temp.append(pq.pop())
      print (temp[-1], end=" ")
   
   print ("\nIn ascending order?", temp == sorted(temp))

if __name__ == '__main__':
   main()
