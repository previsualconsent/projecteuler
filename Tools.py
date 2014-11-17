import itertools
import string
import time
   
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

def digitalSum(n):
    return sum( [int(d) for d in str(n)] )

def gcd(a,b,c=0):
    c+=1
    if a == 0 or b == 0:
        return 1
    if a == b:
        return a
    elif a > b:
        return gcd(a-b,b,c)
    else:
        return gcd(a,b-a,c)

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

from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end







