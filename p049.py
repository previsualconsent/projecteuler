import Prime as p

primeset = set(p.prime_seive(9999))


def is_permutation(one,two):
   return sorted(str(one)) == sorted(str(two))

for i in range(p.n_primes):
   if p.primes[i] < 1000 : continue
   for j in range(i+1,p.n_primes):
      if p.primes[j] < 1000 : continue
      if not is_permutation(p.primes[i], p.primes[j]):
         continue
      third = 2*p.primes[j] - p.primes[i]
      if third in primeset and is_permutation(p.primes[j],third):
         print p.primes[i], p.primes[j],third



