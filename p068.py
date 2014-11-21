
from itertools import permutations

def eval_ngon_ring(i,numbers):
   """ first half is external, second half is internal ring """
   n = len(numbers)/2
   return numbers[i] + numbers[n+i] + numbers[n+(i+1)%n]


def print_ring(numbers):
   """ format in the required order """
   n = len(numbers)/2
   l = [ (numbers[i] , numbers[n+i] , numbers[n+(i+1)%n] )  for i in range(n) ]
   l = [ str(a) + str(b) + str(c) for a,b,c in l]
   return "".join(l)

def check_order(numbers):
   """ make sure it starts with the lowest external number """
   return numbers[0] != min(numbers[:len(numbers)/2])

n = 5
target_length = 16
results = set()
for p in permutations(range(1,1+n*2)): # check everything
   if check_order(p): continue  # only use permutations that start with external min
   magic_n = eval_ngon_ring(0,p) 
   for i in range(1,n):
      if magic_n != eval_ngon_ring(i,p): # if one magic number doesn't match, quit
         break
   else:
      ring_string = print_ring(p) # check length and store as int
      if len(ring_string) == target_length:
         results.add(int(ring_string))

print "Maximum of", len(results), "solutions is", max(results)






