import numpy as np

def decimal_cycle(n):
   if n <= 0:
      return 0
   i = 1
   a = 1
   numerators = {a:i}
   while a%n:
      i += 1
      a = a * 10 % n 
      if a in numerators:
         return i - numerators[a]
      numerators[a] = i
   return 0


max_cycle = 0
cycles = np.array([ decimal_cycle(i) for i in range(1000)] )

print max(cycles)
print cycles.argmax()


