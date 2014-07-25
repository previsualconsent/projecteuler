import math
import Prime

for i in range(2,21):
   fac, n =  Prime.factor(i)
   for k in fac:
      factors[k] = max(factors[k],fac[k])

mmm = p.factdict2list(factors)

print reduce(lambda x, y: x*y, mmm)


