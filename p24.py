from itertools import permutations


def listton(l):
   ret = 0
   p = 0
   for i in reversed(l):
      ret += i*10**p
      p += 1
   return ret

n = 0
millionth = 999999
for p in permutations(range(10)):
   if n >= millionth:
      print listton(p)
      break
   n+= 1



