import  numpy as np
#matrix = np.array([
#      [131,  673,  234,  103,  18],
#      [201,  96,   342,  965,  150],
#      [630,  803,  746,  422,  111],
#      [537,  699,  497,  121,  956],
#      [805,  732,  524,  37,   331]
#      ])
matrix = np.array([map(int,line.split(",")) for line in open("p081_matrix.txt")])

path = np.zeros((len(matrix),len(matrix)))
for i in range(len(path)):
   for j in range(len(path)):
      path[i][j] = float('inf')

path[0][0] = matrix[0][0]
for diagonal in range(len(matrix)*2 -1):
   for i in range(diagonal):
      j = diagonal -1 -i
      if i >= len(matrix) or j >= len(matrix): continue
      if i+1 < len(matrix):
         isum = path[i][j] + matrix[i+1][j]
         path[i+1][j] = min(path[i+1][j], isum)
      if j+1 < len(matrix):
         isum = path[i][j] + matrix[i][j+1]
         path[i][j+1] = min(path[i][j+1], isum)
print path[-1][-1]
