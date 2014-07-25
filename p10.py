import Prime
from time import time

s = time()
print sum(Prime.prime_seive(2000000))

print time() - s

