import itertools
import string
   
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

