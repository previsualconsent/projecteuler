from Tools import repeating_fraction_sqrtn
from math import sqrt


count = 0
for i in range(2,10000):
   if not i % 1000: print i
   if round(sqrt(i))**2 == i:
      continue
   start, loop = repeating_fraction_sqrtn(i)

   if len(loop) % 2 == 1:
      count += 1
print count

