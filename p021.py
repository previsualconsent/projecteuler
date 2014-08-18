import Prime

def d(n):
   div = Prime.factor(n).getdivisors()
   return sum(div)

pairs  = set()

Prime.prime_seive(1000)
for i in range(2,10000):
   if not i in pairs:
      if i == d(d(i)):
         if not i == d(i):
            pairs.add(i)
            pairs.add(d(i))

print pairs
print sum(pairs)

