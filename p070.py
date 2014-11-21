import Tools
import Prime

n = 10**7
Prime.prime_seive(n)
print  min( [ (n/float(t),n,t) for n,t in Prime.totient(n) if Tools.is_perm(n,t) ])

