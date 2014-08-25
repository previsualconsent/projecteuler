import Prime

from Tools import pandigitals

max_pan = 0
# Note: for n=8,9 all pandigitals are divisible by 9
primeset = set(Prime.prime_seive(int(1e7)))
for i in [7,6,5,4,3,2,1]:
   for p in pandigitals(i):
      if p in primeset:
         max_pan = max(p,max_pan)
   if max_pan:
      print max_pan
      break


