import numpy as np

def nrect(x,y):
   return x*(x+1)*y*(y+1)/4

def y(x):
   """
   solve 2e6 == nrect(x,y)
   """
   return -(-np.sqrt(x**2 + 2*x + 32000001 + 32000000/x) + x+1)/(2*x+2)



x = 1.0

results = []
while y(x) >= x:
   yf = np.floor(y(x))
   yc = np.ceil(y(x))

   results += [ (abs(nrect(x, yf) - 2e6), x, yf)]
   results += [ (abs(nrect(x, yc) - 2e6), x, yc)]

   x +=1.0

results.sort()

_, x, y = results[0]

print "{} x {} = {}, N Rectangles = {}".format(x,y,x*y, nrect(x,y))
