
def isPalindrome(n):
   n_str = str(n)
   i = len(n_str)/2
   return n_str[:i] == n_str[-1:-1-i:-1]

print max( [ i * j for i in xrange(100,1000) for j in xrange(100,1000) if isPalindrome(i*j) ] )

