import Prime

n = 1000000
Prime.prime_seive(n)
ps = set(Prime.primes)

#res = (0,0)
#for i in xrange(2,n+1):
#   #if i in ps:
#      #continue
#   if not i % 10000:
#      print i,'/',n
#   phi = 0
#   rp = Prime.rel_primes(i)
#   phi = len(rp)
#   res = max( (float(i)/phi,i), res)
#
#print res

for i in range(150000,151000):
   l = len( Prime.rel_primes(i))

