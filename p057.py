from Tools import bin_gcd

import sys
sys.setrecursionlimit(3000)

a = 3
b = 2

count = 0
for i in xrange(1,1000):
    c = a + 2*b
    d = a + b
    g = bin_gcd(c,d)
    a = c/g
    b = d/g
    if len(str(a)) > len(str(b)):
        count +=1
print count


