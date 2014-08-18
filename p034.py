import math
import numpy as np
from time import time

def ntolist(number):
   ret = []
   while number:
      ret.append(number % 10)
      number /= 10
   return ret

factorial = np.array([math.factorial(i) for i in range(10)])
print factorial

total = 0
ta = 0
tb = 0
tc = 0
for i in range(3,1000000):
   t = time()
   ilist = ntolist(i)
   isum = 0
   ta += time() - t
   for a in ilist:
      isum += factorial[a]
   tb += time() - t
   if i == isum:
      print i
      total +=i
   tc += time() - t

print total

print ta
print tb - ta
print tc - tb
