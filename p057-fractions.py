from Fraction import Fraction
import sys

sys.setrecursionlimit(3000)

f = Fraction(1,2) + 1
count = 0
for i in xrange(1,1000):
    f = 1/(f + 1) + 1
    if len(str(f.num)) > len(str(f.den)):
        count += 1

print count
