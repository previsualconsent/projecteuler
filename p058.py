#!/usr/bin/python2
import Prime
import math

def corners(max_n):
    for n in xrange(1,max_n+1):
        odd = 2*n+1
        d = 2*n
        for i in xrange(odd**2 - 3*d, odd**2+1, d):
            yield i

n = 13500

Prime.prime_seive((2*n+1)**2)

iprime = 0
n_primes = 0.
total = 0.
for c in corners(n):
    for i in xrange(iprime,Prime.n_primes):
        if Prime.primes[i] == c:
            n_primes += 1.
            break
        elif Prime.primes[i] > c:
            break
    iprime = i

    #pf = Prime.primeFactors(c)
    #if Prime.primeFactors(c).isPrime():
        #n_primes += 1.
    total += 1.
    if not total % 1000: print n_primes/total
    
    if not total % 4:
        #print "checking", c, math.sqrt(c),n_primes,(total+1)
        if n_primes/(total+1) < .1: break

print c,math.sqrt(c),n_primes/(total+1)

