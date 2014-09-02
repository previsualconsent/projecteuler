import Prime
from itertools import count

primeset = set(Prime.prime_seive(10000))

for i in xrange(3,10000,2):
   if i in primeset : continue

   winner = False
   for b in count(1):
      doublesquare = 2*b**2
      if i - doublesquare <= 0:
         winner= True
         break
      if i - doublesquare in primeset : 
         break

   if winner:
      print "Winner: %d = 2*%d^2 + %d"%(i,b,i-doublesquare)
      break
