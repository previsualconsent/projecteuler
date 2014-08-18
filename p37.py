
import Prime

primeset = set(Prime.prime_seive(999999))

total = 0
for p in primeset:
   #left
   pstr = str(p)
   if len(pstr) == 1 : continue
   truncatable = True
   for i in range(1,len(pstr)):
      if not int(pstr[-i:]) in primeset : truncatable = False
      if not int(pstr[:i]) in primeset : truncatable = False
   if truncatable:
      print p
      total += p
print total
