import Prime
import numpy as np
from time import time

t = time()
n = 28123
Prime.prime_seive(n)
print time() - t, "seconds"

abundant = np.zeros(n)

abundant = np.where([False,False,False,False] + [ sum(Prime.primeFactors(i).getdivisors()) > i for i in xrange(4,n) ])[0]

print "# of abundant #'s",len(abundant)
print time() - t, "seconds"

abundant_sums = set()
for i in xrange(len(abundant)):
   for j in xrange(i,len(abundant)):
      abundant_sums.add( abundant[i] + abundant[j] )

print "# of #'s that can be written as the sum of two abundunt #'s", len(abundant_sums)
print time() - t, "seconds"
non_abundant_sums = set(range(n)) - abundant_sums
print "# of of #'s that cannot be written as the sum of two abundunt #'s", len(non_abundant_sums)
print "Sum of that", sum(non_abundant_sums)
print time() - t, "seconds"
