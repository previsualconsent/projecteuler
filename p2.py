
x = 1
y = 2

total = 0
while y < 4e6:
   if not y % 2:
      total += y
   n = x + y 
   x = y
   y = n

print total
