
def isPalindrome(n):
   i = len(n)/2
   return n[:i] == n[-1:-1-i:-1]

total = 0
for i in xrange(1000000):
   if isPalindrome(str(i)):
      b = bin(i)[2:]
      if isPalindrome(b):
         print i, b
         total += i

print total
