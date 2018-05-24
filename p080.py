import math


def sqrt_gen(n):
   c = n
   p = ""
   p2 = ""

   while len(str(p)) < 100:
      #x = int(-10*int(p) + math.sqrt(c+100*int(p)**2))
      #y = x*(20*int(p) + x)

      #if not p: p = str(x)
      #else: p += str(x)
      #r = c - y
      #c = r*100
      if not p:
         x = int(math.sqrt(c))
         y = x*x
      else:
         x = int(c/(20*float(p)))
         y = x*(20*int(p) + x) 
         while y > c:
            x -= 1
            y = x*(20*int(p) + x) 
         while y <= c:
            nx = x + 1
            ny = nx*(20*int(p) + nx) 
            if ny <= c:
               x = nx
               y = ny
            else:
               break

      #p = addDigit(p+"0",x)
      #p2 = addDigit(p2 + "0",x*2)
      p += str(x)
      r = c - y
      if r == 0: return 0
      c = r*100

   return sum(map(int,p))

total = 0
for i in range(101):
   total += sqrt_gen(i)
   print i,total
