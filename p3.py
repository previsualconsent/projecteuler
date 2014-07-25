import math
import Prime

n = 600851475143
p = Prime.Primes()

factors = []
while not n == 1:
   p.make_primes(int(math.sqrt(n)))
   fac, n = p.factor(n)
   factors += p.factdict2list(fac)
   print factors, n
