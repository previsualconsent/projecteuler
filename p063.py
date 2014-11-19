
def power_length(b,p):
   return len(str(b**p))

count = 0
for p in range(1,22):
   b = 1
   while power_length(b,p) < p:
      b += 1
   while power_length(b,p) ==  p:
      print "%d^%-2d = %d" %(b,p, b**p)
      b += 1
      count += 1

print count

