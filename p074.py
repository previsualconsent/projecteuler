import math
def get_next(n, map={}):
   map[n] = sum( [ math.factorial(int(c)) for c in str(n)])
   return map[n]

def make_chain(n, chain_map={}):
   chain = [n]
   while chain.count(chain[-1]) == 1:
      if chain[-1] in chain_map:
         chain += chain_map[chain[-1]][1:]
      else:
         chain.append(get_next(chain[-1]))
   chain_map[n] = chain
   return chain

def get_nonrepeating(n):
   return len(make_chain(n)) - 1

from collections import defaultdict
results = defaultdict(list)
for i in xrange(1000000):
   if not i % 10000: print i
   results[get_nonrepeating(i)].append(i)

m = max(results)
print m, results[m], len(results[m])
