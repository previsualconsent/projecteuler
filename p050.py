import Prime

n = 1000000
primeset = set(Prime.prime_seive(n))



total = 0
for max_n,p in enumerate(Prime.primes):
   total += p
   if total > n:
      break

l = max_n

lb = 5
while l > lb:
   for i in range(Prime.n_primes - l + 1):
      s = sum(Prime.primes[i:i+l]) 
      if s > n :
         break
      if sum(Prime.primes[i:i+l]) in primeset:
         print l,Prime.primes[i:i+l],sum(Prime.primes[i:i+l])
         l = lb
         break

   l -= 1


