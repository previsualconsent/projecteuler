import  numpy as np
from timeit import default_timer as timer

matrix = np.array([
      [131,  673,  234,  103,  18],
      [201,  96,   342,  965,  150],
      [630,  803,  746,  422,  111],
      [537,  699,  497,  121,  956],
      [805,  732,  524,  37,   331]
      ])
#matrix = np.array([map(int,line.split(",")) for line in open("p082_matrix.txt")])
path = np.zeros((len(matrix),len(matrix)))
for i in range(len(path)):
   for j in range(len(path)):
      path[i][j] = float('inf')

path[:,0] = matrix[:,0]
for col in range(1,len(matrix)):
   for row in range(len(matrix)):
      for lastrow in range(len(matrix)):
         if row > lastrow:
            irows = range(lastrow,row+1)
         else:
            irows = range(row,lastrow+1)
         cost = path[lastrow,col-1] + sum(matrix[irows,col])
         path[row,col] = min(path[row,col], cost )

print path
print min(path[:,-1])
