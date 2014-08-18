from itertools import product

def listton(l):
   ret = 0
   p = 0
   for i in reversed(l):
      ret += i*10**p
      p += 1
   return ret

def powersum(l,p):
   return sum( [ i**p for i in l] )


total = 0
for p in product(range(10),repeat=6):
   n = listton(p)
   if n == powersum(p,5) and not n == 0 and not n == 1:
      print n
      total += n

print total



