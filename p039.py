import math
import numpy as np

combinations = np.zeros(1001)

def perimeter(a,b):
   return a + b + math.sqrt(a**2 + b**2)

for a in xrange(1,1000):
   for b in xrange(a,1000):
      p = perimeter(a,b)
      if p <= 1000:
         if int(p) == p:
            combinations[int(p)] +=1

print combinations.argmax()
print combinations[combinations.argmax()]
