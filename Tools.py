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
