import  numpy as np
from timeit import default_timer as timer

matrix = np.array([
      [131,  673,  234,  103,  18],
      [201,  96,   342,  965,  150],
      [630,  803,  746,  422,  111],
      [537,  699,  497,  121,  956],
      [805,  732,  524,  37,   331]
      ])
realpath  = np.array(
      [
         [  131.,   804.,   873.,   976.,   994.],
         [  201.,   297.,   639.,  1604.,  1144.],
         [  630.,  1100.,  1385.,  1807.,  1255.],
         [  537.,  1236.,  1733.,  1854.,  2211.],
         [  805.,  1537.,  2061.,  1891.,  2222.],]
      )
matrix = np.array([map(int,line.split(",")) for line in open("p082_matrix.txt")])
path = np.zeros((len(matrix),len(matrix)))
for i in range(len(path)):
   for j in range(len(path)):
      path[i][j] = float('inf')

path[:,0] = matrix[:,0]
for col in range(1,len(matrix)):
   for row in range(len(matrix)):
      upsum = 0
      for lastrow in range(row, len(matrix)):
         upsum += matrix[lastrow,col]
         cost = path[lastrow,col-1] + upsum
         path[row,col] = min(path[row,col], cost )
      downsum = matrix[row,col]
      for lastrow in range(row-1, -1,-1):
         downsum += matrix[lastrow,col]
         cost = path[lastrow,col-1] + downsum
         path[row,col] = min(path[row,col], cost )
   #if not (path[:,:col+1] == realpath[:,:col+1]).all(): break


#print path[:,:col+1] - realpath[:,:col+1]

print min(path[:,-1])
