
from itertools import permutations

n = 9

def listton(l):
   ret = 0
   p = 0
   for i in reversed(l):
      ret += i*10**p
      p += 1
   return ret

results = set()
for l in permutations(range(1,n+1),n):
      for i in range(1,3):
         j = 5
         a = listton(l[0:i])
         b = listton(l[i:j])
         c = listton(l[j:])
         if a*b == c:
            print a,b,c
            results.add(c)

print "Answer:",sum(results)

