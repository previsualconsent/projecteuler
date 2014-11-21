from fractions import Fraction

max_d = 10**6

rpfs = []
best = Fraction(0,1)
for d in xrange(2,max_d+1):
   if not d%10000: print d,'/',max_d

   for n in xrange(int(best*d)+1, d):
      if float(n)/d < 3./7:
         if best != Fraction(n,d):
            #print best, float(best)
            best = Fraction(n,d)
      else:
         break

print best

