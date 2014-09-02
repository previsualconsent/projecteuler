import math
def choose(n,r):
   return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

count = 0
for n in range(1,101):
   for r in range(1,n):
      if choose(n,r) > 1000000:
         count += 1
print count
