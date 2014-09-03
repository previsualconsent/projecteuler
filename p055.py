from Tools import reverseInt,isPalindrome
import time

def nrevn(n):
   strn = str(n)
   l = len(strn)
   ret = 0
   for i in range(l-1,-1,-1):
      ret += n*int(strn[i])*10**i
   return ret

count = 0


t1 = 0
t2=  0
for n in xrange(1,10000):
   a = n + reverseInt(n)
   for i in xrange(1,50):
      if isPalindrome(str(a)):
         break
      a = a + reverseInt(a)
   else:
      count += 1

print count
