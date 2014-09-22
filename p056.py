
from Tools import digitalSum

max_sum = 0

for a in xrange(100):
    for b in xrange(100):
        max_sum = max(max_sum, digitalSum(a**b))

print max_sum
