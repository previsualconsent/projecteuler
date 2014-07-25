
n_paths = 0

class vertex:
   def __init__(self,x,y,n):
      self.x = x
      self.y = y
      self.n = n
      #we got to the end, increment
      if self.x == self.n and self.y == self.n:
         global n_paths
         n_paths += 1
         if not n_paths % 100000:
            print n_paths
      else:
         if self.x < self.n:
            vertex(self.x+1,self.y,self.n)
         if self.y < self.n: 
            vertex(self.x,self.y+1,self.n)

#recursively build all paths
v = vertex(0,0,20)

print n_paths



