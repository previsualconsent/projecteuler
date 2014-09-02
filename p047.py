import Prime
from itertools import count

n = 1000

res = []
for a in count(2):
   f = Prime.factor(a)
   if len(f.factors) == 4:
      res.append(a)
      if len(res) == 4:
         print res
         break
   else:
      res = []




