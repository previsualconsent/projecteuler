import numpy as np
import math

      
n_primes = 4
primes = np.array([2,3,5,7])

def getNPrimes(n):
   """ iterable that returns n primes """
   global primes
   global n_primes

   for p in primes[:n]:
      yield p
   new_p = primes[-1] +2
   pl = list(primes)
   while(len(pl)< n):
      for p in pl:
         if not new_p % p:
            new_p += 2
            break
         if p*p > new_p:
            pl.append(new_p)
            yield new_p
            new_p += 2
            break
   primes = np.append(primes, pl[len(primes):])
   n_primes = primes.size

def prime_seive(n):
   global primes
   global n_primes

   if n < primes[-1]:
      return primes
   isPrime =  np.ones(n,dtype=bool)
   isPrime[0:2] = False
   max_n = int(math.ceil(math.sqrt(n)))
   for i in xrange(2,max_n):
      if not i % 100:
         print "Seiving [%d/%d]"%(i,max_n)

      if isPrime[i]:
         isPrime[ i*i : n + 1 : i ] = False #multiples of i from i^2 to n are not prime

   primes = np.where(isPrime)[0]
   n_primes = primes.size
   return primes


class primeFactors:
   def __init__(self,n):
      if type(n) == int or type(n) == np.int64:
         self.factors = {}
         for p in primes:
            while not n % p:
               self.addfactor(p)
               n /= p
            if n == 1 : break
            #if n in primeset:
            #   self.addfactor(n)
            #   n = 1
            #   break
         if (not n == 1) and primes[-1]**2 > n:
               self.addfactor(n)
               n = 1
      elif type(n) == dict:
         self.factors = n
      else:
         print type(n), "is not supported"

   def addfactor(self,p):
      if p in self.factors:
         self.factors[p]+=1
      else:
         self.factors[p]=1

   def getlist(self):
      ret = []
      d = self.factors.items()
      d.sort()
      for a,b in d:
         ret += [a]*b
      return ret
   def getNdivisors(self):
      return np.prod( np.array(self.factors.values()) + 1)

   def getdivisors(self):
      divisors = [1]
      for p in self.factors:
         newd = []
         for i in divisors:
            newd += [i*p**l for l in range(0,self.factors[p]+1) ]
         divisors = newd
      divisors.sort()
      return divisors[:-1]

   def LCM(self,other_pf):
      retdict = self.factors.copy()

      for i in other_pf.factors:
         if i in retdict:
            retdict[i] = max( self.factors[i],other_pf.factors[i])
         else:
            retdict[i] = other_pf.factors[i]
      return primeFactors(retdict)

   def GCD(self,other_pf):
      retdict = self.factors.copy()
      for i in retdict:
         if i in other_pf.factors:
            retdict[i] = min(self.factors[i],other_pf.factors[i])
         else:
            retdict.pop(i)
      return primeFactors(retdict)
   def getValue(self):
      ret = 1
      for i in self.factors:
         ret *= i**self.factors[i]
      return ret


         

   def __repr__(self):
      return self.__str__()
   def __str__(self):
      d = self.factors.items()
      d.sort()
      retstr = ""
      for (b,p) in d:
         retstr+= "%d^%d * " %(b,p)
      return retstr[:-3]
   

def factor(n):
   prime_seive(int(math.ceil(math.sqrt(n))))
   return primeFactors(n)
