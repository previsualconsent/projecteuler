

def corners(n):
   x = 1
   yield x
   for a in xrange(2,n+1,2):
      yield x + a
      yield x + 2*a
      yield x + 3*a
      yield x + 4*a
      x += 4*a

print sum ( [i for i in corners(5) ] )
print sum ( [i for i in corners(1001) ] )
