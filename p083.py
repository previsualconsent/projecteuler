import  numpy as np
from timeit import default_timer as timer

matrix = np.array([
      [131,  673,  234,  103,  18],
      [201,  96,   342,  965,  150],
      [630,  803,  746,  422,  111],
      [537,  699,  497,  121,  956],
      [805,  732,  524,  37,   331]
      ])
matrix = np.array([
      [001,  100,  001,  001,  001],
      [001,  100,  001,  100,  001],
      [001,  100,  001,  100,  001],
      [001,  100,  001,  100,  001],
      [001,  001,  001,  100,  001]
      ])

matrix = np.array([
      [001,  100,  050,  001,  001],
      [001,  010,  001,  100,  001],
      [001,  100,  001,  100,  001],
      [001,  010,  001,  100,  001],
      [001,  100,  001,  100,  001]
      ])

""" 
New idea

make a graph of all possible routes. prefer minimum costs, if you hit a dead end or reach the end, go back to last fork
follow fork until you meet with a point thats already on the route. if your total is smaller, that whole tree. 
while updating check if any of the points have been already updated to a better minimum

"""

class Graph:
   points = set()
   def __init__(self, matrix):
      i,j = 0,0
      self.head = Node(matrix[i,j],(i,j),None)
      self.matrix = matrix
   def getChildren(self, node):

      neighbors = [[total + matrix[x,y],x,y] for x,y in [ (i+1,j), (i-1,j), (i,j+1), (i,j-1) ] 
         if x >=0 and y>=0 and x < len(matrix) and y < len(matrix) and status[x,y]!=0]


class Node:
   def __init__(self, cost, index,parent):
      self.cost = cost
      self.index = index
      self.parent = parent
      self.children = children
      self.checked = [False]*len(self.children)


"""
#TRIED TAKING MINIMUMS AND AVOIDING DEADENDS
#NEED TO CHECK ALTERNATE ROUTES FOR BETTER MINIMUM
matrix = np.array([map(int,line.split(",")) for line in open("p083_matrix.txt")])
sums = np.zeros((len(matrix),len(matrix)))
status = np.zeros((len(matrix),len(matrix)))
#unvisited 0 
#visisted 1
#options 2

i,j = 0,0
end = len(matrix)-1, len(matrix)-1
total = matrix[i,j]
maxi, maxj = 0,0

torevisit = []
while not (i,j) == end:
   status[i,j] = 1
   options = [[total + matrix[x,y],x,y] for x,y in [ (i+1,j), (i-1,j), (i,j+1), (i,j-1) ] 
         if x >=0 and y>=0 and x < len(matrix) and y < len(matrix) and status[x,y]!=0]
   if not options:
      total,i,j = torevisit.pop()
      sums[i,j] = total
      continue

   options.sort(reverse=True)
   total, i,j = options.pop()
   if status[i,j] == 2 and total < sums[i,j]:
      status[i,j] == 1kkkkkkku
   torevisit.extend(options) 
   for val,x,y in options:
      if (x,y) == (i,j):continue
      status[x,y]  = 2
      sums = val
   maxi = max([maxi, i])
   maxj = max([maxj, j])
   sums[i,j] = total
for i in range(len(status)):
   for j in range(len(status)):
      print "%7d |" % status[i,j],
   print
   for j in range(len(status)):
      print "%7d |" % matrix[i,j],
   print
   for j in range(len(status)):
      print "%7d |" % sums[i,j],
   print
   for j in range(len(status)):
      print "---------",
   print
"""
