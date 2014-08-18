import Prime
from collections import deque


primeset = set(Prime.prime_seive(1000000))

circulars = set()
for p in primeset:
   strp = deque(str(p))
   cycles = set()
   isCircular = True
   for i in range(len(strp)):
      strp.rotate(1)
      i = int(''.join(map(str, strp)))
      if i in primeset:
         cycles.add(i)
      else:
         isCircular = False
   if isCircular:
      circulars = circulars | cycles


print (circulars, len(circulars))






