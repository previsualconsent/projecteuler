import  numpy as np
from timeit import default_timer as timer
import sys

sys.setrecursionlimit(15000)

matrix = np.array([
      [131,  673,  234,  103,  18],
      [201,  96,   342,  965,  150],
      [630,  803,  746,  422,  111],
      [537,  699,  497,  121,  956],
      [805,  732,  524,  37,   331]
      ])
matrix = np.array([map(int,line.split(",")) for line in open("p083_matrix.txt")])

#Slow search using a graph
# Make graph
#nodes = []
#distances = {}
#for i in range(len(matrix)):
#   for j in range(len(matrix)):
#      nodes += [(i,j)]
#      distances[(i,j)] = {(x,y):matrix[x,y] for x,y in [ (i+1,j), (i-1,j), (i,j+1), (i,j-1) ] 
#                           if x >=0 and y>=0 and x < len(matrix) and y < len(matrix)}
#
#unvisited = {node: float("inf") for node in nodes} 
#visited = {}
#current = (0,0)
#currentDistance = matrix[current]
#unvisited[current] = currentDistance
#
#while True:
#    for neighbour, distance in distances[current].items():
#        if neighbour not in unvisited: continue
#        newDistance = currentDistance + distance
#        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
#            unvisited[neighbour] = newDistance
#    visited[current] = currentDistance
#    del unvisited[current]
#    if not unvisited: break
#    candidates = [node for node in unvisited.items() if node[1]]
#    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
#
#print visited[(len(matrix)-1, len(matrix)-1)]


#Fast exploiting grid nature
minpath = np.zeros((len(matrix), len(matrix)))
for i in range(len(matrix)):
   for j in range(len(matrix)):
      minpath[i,j] = float('inf')
minpath[0,0] = matrix[0,0]
last = None
while last != minpath[len(matrix)-1, len(matrix)-1]:
   last = minpath[len(matrix)-1, len(matrix)-1]
   for i in range(len(matrix)):
      for j in range(len(matrix)):
         for x,y in [ (i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if x >=0 and y>=0 and x < len(matrix) and y < len(matrix):
               if minpath[x,y]:
                  minpath[i,j] = min(minpath[i,j], minpath[x,y]+matrix[i,j])
   print minpath



