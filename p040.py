from itertools import count

def champernowne(max_n):

   n = 0
   for i in count(1):
      for a in str(i):
         n += 1
         yield int(a),n
         if n == max_n:
            return

l = [10**i for i in range(7)]

res = 1
for i,n in champernowne(l[-1]):
   if n in l:
      print i
      res *= i

print res



