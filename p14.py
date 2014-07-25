import numpy as np

def collatz(n):
   if n % 2:
      return 3*n +1
   else:
      return n/2

collatz_length = {1:1}

#for i in range(1000000, 2, -1):
for i in range(2,1000000):
   chain = []

   while not i in collatz_length:
      chain.append(i)
      collatz_length[i] = 0
      for c in chain:
         collatz_length[c] += 1
      i = collatz(i)
   else:
      for c in chain:
         collatz_length[c] += collatz_length[i]

print collatz_length.keys()[np.argmax(collatz_length.values())]
