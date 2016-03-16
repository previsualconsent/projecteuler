def count_perm(n, max_sub, res = {(0,0):1}):
   if (n,max_sub) in res:
      return res[(n,max_sub)]
   if n == 1 or max_sub == 1:
      res[(n,max_sub)] = 1
      return 1
   p = 0
   for i in xrange(max_sub,0,-1):
      p += count_perm(n - i,min(i,n-i))
   res[(n,max_sub)] = p
   return p

print count_perm(100,99)
