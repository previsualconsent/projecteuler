from Tools import bin_gcd
from collections import defaultdict

res = defaultdict(int)
max_l = 1500000
max_m = 0 
max_n = 0
for m in xrange(1,612):
   for n in xrange(m+1,867,2):
      if bin_gcd(m,n) == 1: 
         #a = n**2 - m**2
         #b = 2 * m * n 
         #c = m**2 + n**2
         l = 2*n**2 + 2 * m * n  
         for k in xrange(1,max_l/l+1):
         #for k in xrange(1,2):
            if l*k <= max_l:
               max_m = max(m,max_m)
               max_n = max(n,max_n)
               res[l*k] += 1

print max_m
print max_n
print sum( [ 1 for l,n in res.items() if n == 1]) 

