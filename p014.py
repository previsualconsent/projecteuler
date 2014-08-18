import numpy as np

#def collatz(n):
#   if n % 2:
#      return 3*n +1
#   else:
#      return n/2

def collatz(n):
   if n & 1:
      return n+(n<<1)+1
   else:
      return n>>1

collatz_length = {1:1}

for i in range(2,1000000):
   chain = []

   while not i in collatz_length:
      chain.append(i)
      i = collatz(i)
   else:
      for n,c in enumerate(reversed(chain)):
         collatz_length[c] = collatz_length[i] + n

print collatz_length.keys()[np.argmax(collatz_length.values())]
