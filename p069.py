import Prime

n = 1000000
Prime.prime_seive(n)

print max([ (n/float(t),n) for n,t in Prime.totient(n) ])


