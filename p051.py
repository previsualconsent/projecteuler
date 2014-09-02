import Prime
from itertools import permutations

max_prime = 10000000
ps = set(Prime.prime_seive(max_prime))

done = False
for p in Prime.primes:
   pstr = str(p)
   for d in set(pstr):
      family = []
      for i in "0123456789":
         f = int(pstr.replace(d,i))
         if not len(str(f)) == len(pstr):
            continue
         if f in ps:
            family.append(f)
      if len(family) == 8:
         done = True
         print family
         break
   if done : break




