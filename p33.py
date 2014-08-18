import Prime
import numpy as np

numerators = []
denominators = []
for i in np.arange(1,10, dtype = float):
   for a in np.arange(1,10, dtype = float):
      for b in np.arange(1,10, dtype = float):
         if a == b : continue
         if (i*10+a)/(i*10+b) == a/b and (i*10+a)/(i*10+b) < 1:
            print (i*10+a),'/',(i*10+b)
            numerators.append(i*10+a)
            denominators.append(i*10+b)
         if (i+a*10)/(i*10+b) == a/b and (i+a*10)/(i*10+b) < 1:
            print (i+a*10),'/',(i*10+b)
            numerators.append(i+a*10)
            denominators.append(i*10+b)
         if (i+a*10)/(i+b*10) == a/b and (i+a*10)/(i+b*10) < 1:
            print (i+a*10),'/',(i+b*10)
            numerators.append(i+a*10)
            denominators.append(i+b*10)
         if (i*10+a)/(i+b*10) == a/b and (i*10+a)/(i+b*10) < 1:
            print (i*10+a),'/',(i+b*10)
            numerators.append(i*10+a)
            denominators.append(i+b*10)

top = int(np.prod(numerators))
bot = int(np.prod(denominators))

Prime.prime_seive(max(top,bot))

pt = Prime.primeFactors(top)
pb = Prime.primeFactors(bot)
gcd = pt.GCD(pb).getValue()

print top,bot,gcd
print top/gcd, bot/gcd
