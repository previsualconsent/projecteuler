from fractions import Fraction
from Tools import repeating_fraction_sqrtn, repeating_fraction_conv
from math import sqrt

max_depth = 100

max_x = 0
max_D = 0

# using this algorithm
# http://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions

for D in xrange(2,1001):
   if round(sqrt(D))**2 == D:
      continue
   for f in repeating_fraction_conv(repeating_fraction_sqrtn(D), max_depth):
      if f.numerator**2 - D * f.denominator**2 == 1:
         #print "%d^2 - %d x %d^2 = 1" % (f.numerator,D, f.denominator)
         if max_x < f.numerator:
            max_x = f.numerator
            max_D = D
         break
   else:
      print "max_depth too low", max_depth
      raw_input()

print max_D




