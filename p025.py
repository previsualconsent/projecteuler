import math

def lessthan1000digits(n):
   return math.ceil(math.log(n,10)) < 1000

def fib(a,b):
   yield a
   yield b
   n = a + b
   while True:
      yield n
      a = b
      b = n
      n = a + b

n = 1
for i in fib(1,1):
   if not lessthan1000digits(i):
      break
   n+=1

print i,n
