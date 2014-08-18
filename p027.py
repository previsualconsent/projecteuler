import Prime

def quad_prime(a,b,prime_set):
   n = 0
   x =  n**2 + a*n + b 
   while x in prime_set:
      x =  n**2 + a*n + b 
      yield x
      n+=1
      



Prime.prime_seive(100000)
prime_set = set(Prime.primes)

maximum = (0, 0, 0)
for b in Prime.primes:
   length = 0
   if b > 1000:
      break
   for a in xrange( 1-b, 1000 ):
      l = len([p for p in quad_prime(a,b,prime_set) ] )
      maximum = max(maximum,(l,a,b))



print maximum, maximum[1]*maximum[2]
