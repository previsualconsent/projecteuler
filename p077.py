import Prime

#def count_perm(n, max_sub, res = {(0,0):1,(2,2):1,(3,3):1}):
def count_perm(n, max_sub, res = {(0,0):1}):
   if (n,max_sub) in res:
      return res[(n,max_sub)]
   p = 0
   for i in Prime.primesLessThan(max_sub):
      c = count_perm(n - i,min(i,n-i))
      p += c
   res[(n,max_sub)] = p
   return p

Prime.prime_seive(100)
from itertools import count
for i in count(10):
   c = count_perm(i,i)
   print i,c
   if c > 5000:
      break
