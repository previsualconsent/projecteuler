#!/usr/bin/python2

import itertools
import numpy as np
import math


def triangle(n):
   return n*(n+1)/2
def square(n):
   return n**2
def pentagon(n):
   return n*(3*n-1)/2
def hexagon(n):
   return n*(2*n-1)
def heptagon(n):
   return n*(5*n-3)/2
def octogan(n):
   return n*(3*n-2)

def is_triangle(n):
    return (-1 + math.sqrt(1 + (8 * n))) % 2 == 0
def is_square(n):
    return int(math.sqrt(n)) == math.sqrt(n)
def is_pentagonal(n):
    return (1 + math.sqrt(1 + (24 * n))) % 6 == 0
def is_hexagonal(n):
    return (1 + math.sqrt(1 + (8 * n))) % 4 == 0
def is_heptagonal(n):
    return (3 + math.sqrt(9 + (40 * n))) % 10 == 0
def is_octagonal(n):
    return (2 + math.sqrt(4 + (12 * n))) % 6 == 0

def gen_4digit(func):
   for i in itertools.count():
      x = func(i)
      if x >= 10000:
         break
      if x >= 1000:
         yield x

   
def check_path(nums):
   if len(nums) < 2:
      return True
   tests = [is_triangle, is_square, is_pentagonal, is_hexagonal, is_heptagonal,is_octagonal]

   res = np.matrix( [ [ test(num)for test in tests] for num in nums] )

   if res.any(0).sum() < len(nums):
      return False

   for i in range(len(nums)):
      a = np.delete(res, [i],axis=0)
      if a.any(0).sum() < len(nums) - 1:
         return False

   return True

   

   
def check_digits(a,b):
   return a % 100 == b / 100

def find_cycle(graph, vertex, cycles, path = []):
   if vertex not in path:
      path.append(vertex)
      for i in graph[vertex]:
         if i not in path and check_path(path + [i]):
            find_cycle(graph,i,cycles,path)
         elif i is path[0] and len(path) == 6:
            for c in cycles:
               if isSameCycle(path + [i], c):
                  break
            else:
               cycles.append(path + [i])
   path.pop()

def isSameCycle(a,b):
   if a == b:
      return True
   if len(a) != len(b):
      return False
   x = a[:-1]
   y = b[:-1]
   for i in range(1,len(x)):
      if y[:i] == x[-i:] and y[i:] == x[:-i]:
         return True
   return False

def findCycles(graph):
   cycles = []
   for i in graph:
      find_cycle(graph,i,cycles)
   return cycles




funcs = [triangle,square,pentagon,hexagon,heptagon,octogan]

candidates = [ [a for a in gen_4digit(func)] for func in funcs]

graph = {}

for i in range(len(candidates)):
   for j in range(len(candidates)):
      if i is not j:
         for a in candidates[i]:
            for b in candidates[j]:
               if check_digits(a,b):
                  if a in graph:
                     graph[a].append(b)
                  else:
                     graph[a] = [b]
                  if b not in graph:
                     graph[b] = []

for cycle in findCycles(graph):
   print cycle,sum(cycle[:-1])

