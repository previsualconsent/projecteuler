import numpy as np



def getpaths(x,y,mat,n):
   if x > n or y > n:
      return 0
   if x == n and y == n:
      mat[x,y] = 1
      return 1
   if not mat[x,y]:
      mat[x,y] = getpaths(x+1,y,mat,n) + getpaths(x,y+1,mat,n)
   return mat[x,y]


   


n = 20
mat = np.zeros((n+1,n+1),dtype = int)

print getpaths(0,0,mat,n)
