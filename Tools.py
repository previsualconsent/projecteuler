import itertools
import string
import time
import math
   
def check_pandigital(n):
   """ check if a string represents a pandigital number """
   for i in range(1,len(str(n))+1):
      if not str(i) in n:
         return False
   return True

def pandigitals(n,zeros = False):
   z = int(zeros)
   for a in itertools.permutations(string.digits[1-z:n+1-z], n):
      yield int(reduce(lambda x,y: x+y,a))

def isPalindrome(n):
   for i in range(len(n)/2):
      if not n[i] == n[-1 -i]:
         return False
   return True
#def isPalindrome(n):
#   """ checks if a list/string is a palindrome """
#   i = len(n)/2
#   return n[:i] == n[-1:-1-i:-1]

def reverseInt(n):
   return int(str(n)[-1::-1])

def is_perm(a,b):
   return sorted(str(a)) == sorted(str(b))

def digitalSum(n):
    return sum( [int(d) for d in str(n)] )

def gcd_list(l):
   return reduce(gcd,l)

gcd_dict = dict()
def gcd(a,b):
    #if (a,b) in gcd_dict:
      #return gcd_dict[(a,b)]
    if a == 0 or b == 0:
        #gcd_dict[(a,b)] = 1
        return 1
    if a == b:
        #gcd_dict[(a,b)] = a
        return a
    elif a > b:
        ret = gcd(a-b,b)
    else:
        ret =  gcd(a,b-a)
    #gcd_dict[(a,b)] = ret
    return ret

def bin_gcd(a,b):
    if not a:
        return b
    if not b:
        return a
    shift = 0
    while (a | b) & 1 == 0:
        a = a >> 1
        b = b >> 1
        shift += 1
    while (a & 1) == 0:
        a = a >> 1

    while True:
        while (b & 1) == 0 :
            b = b >> 1

        if a > b:
            c = b
            b = a
            a = c
        b = b - a

        if b == 0:
            break

    return a << shift

def fibonacci(a,b, max_i):
   if max_i > 0:
      yield a
   if max_i > 1:
      yield b
   n = a + b
   i = 2
   while max_i > i:
      i += 1
      yield n
      a = b
      b = n
      n = a + b

def __rf_helper__(n,n2,a,b):
   x = int ( a / (n2 - b))
   z = (n - b ** 2) / a
   y = abs(b - x * z)
   #print "in: ", (n,n2,a,b)
   #print "out: ", (x,y,z)
   #raw_input()
   return (x,y,z)

def repeating_fraction_sqrtn(n):
   ''' Works at precision 5, farther and it gets things wrong '''
   l = []
   xs = []
   n2 = math.sqrt(n)
   l.append(int(n2))
   a = 1
   b = int(n2)
   
   while (a,b) not in xs:
      xs.append((a,b))
      i,b,a = __rf_helper__(n, n2, a, b)
      l.append(i)

   cycle_point = xs.index((a,b))+1
   return ( l[:cycle_point], l[cycle_point:])

import fractions
def repeating_fraction_conv((start,loop),n):
   ls = len(start)
   ll = len(loop)
   for i in xrange(n):
      f = fractions.Fraction(0)
      for j in xrange(i,-1,-1):
         if j < ls:
            a = start[j]
         else:
            a = loop[ (j - ls) % ll ] 

         if f:
            f = 1/f + a
         else:
            f = fractions.Fraction(a)
      yield f
   
import bisect 
def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect.bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def gen_pent(max):
   from itertools import count
   for i in count(1):
      np = i * (3 * i - 1) / 2
      if np > max: return
      yield (np, (-1)**i)
      nn = - i * (- 3 * i - 1) / 2
      if nn > max: return
      yield (nn, (-1)**i)

def partitions(n, res = {0:1}):
   if n in res:
      return res[n]
   s = 0
   for p,sign in gen_pent(n):
      s -= sign*partitions(n - p) 
   res[n] = s
   return res[n]
