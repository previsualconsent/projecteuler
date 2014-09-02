from time import time

ti = time()
n = 100000
ns = range(n)
#t = set([i*(i+1)/2 for i in xrange(n)])
#p = set([i*(3*i-1)/2 for i in xrange(n)])
#h = set([i*(2*i-1) for i in xrange(n)])
t = set(map(lambda i:i*(i+1)/2,  ns))
p = set(map(lambda i:i*(3*i-1)/2,ns))
h = set(map(lambda i:i*(2*i-1),  ns))

print time() - ti
print t & p & h
print time() - ti
