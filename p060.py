import Prime
from itertools import combinations,permutations
from time import time
import numpy as np
import math

#def cat_ints(a,b):
    #return a*10**(np.floor(np.log10(b))+1) + b

def cat_ints(a,b):
    if b > 100000000:
        res = a*1000000000 + b
    elif b > 10000000:
        res = a*100000000 + b
    elif b > 1000000:
        res = a*10000000 + b
    elif b > 100000:
        res = a*1000000 + b
    elif b > 10000:
        res = a*100000 + b
    elif b > 1000:
        res = a*10000 + b
    elif b > 100:
        res = a*1000 + b
    elif b > 10:
        res = a*100 + b
    else:
        res = a*10 + b

    return res

max_n = 99999999
Prime.prime_seive(max_n)
prime_set = set(Prime.primes)
pairs = {}
print "Making pairs"

ttotal = 0
for i in xrange(Prime.n_primes):
    p1 = Prime.primes[i]
    for j in xrange(i+1, Prime.n_primes):
        ttotal += 1
        p2 = Prime.primes[j]
        #if Prime.isPrime(cat_ints(p1,p2)) and Prime.isPrime(cat_ints(p2,p1)):
        new_p1 = cat_ints(p1,p2) 
        if new_p1 in prime_set:
            new_p2 = cat_ints(p2,p1) 
            if new_p2 in prime_set :
                if p1 in pairs:
                    pairs[p1].add(p2)
                else:
                    pairs[p1] = set([p2])
                if p2 in pairs:
                    pairs[p2].add(p1)
                else:
                    pairs[p2] = set([p1])

        if new_p1 > max_n:
            print p1,p2
            break
    if len(str(p1))*2 > len(str(max_n)): break

print ttotal
print "searching results"
minimum = 0

for a in pairs:
    for b in pairs[a]:
        for c in pairs[a] & pairs[b]:
            for d in pairs[a] & pairs[b] & pairs[c]:
                for e in pairs[a] & pairs[b] & pairs[c] & pairs[d]:
                    new_min = sum([a,b,c,d,e])
                    if new_min < minimum or minimum==0:
                        minimum = new_min
                        res = [a,b,c,d,e]

print res,  minimum



