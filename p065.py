from fractions import Fraction

lb = [[1,2*k,1] for k in range(33,0,-1)]
numbers = [ a for b in lb for a in b]

x = Fraction(1,numbers[0])
for b in numbers[1:]:
   x = 1/(b + x)

x += 2

print x.numerator
print sum([ int(l) for l in str(x.numerator)] )


