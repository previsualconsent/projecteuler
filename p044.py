from itertools import count

def pentagon(n):
   return n*(3*n-1)/2


n = 3000
print "making lists"
pentagons =[ pentagon(n) for n in range(1,n+1)] 
pns = set(pentagons)


print "running over lists up to",pentagons[-1]
end = False
for i in count(1):
   if not i % 100: print i
   for j in xrange(0,n-i):
      if pentagons[j+i] - pentagons[j] in pns and pentagons[j+i] + pentagons[j] in pns:
         print j,",",j+i,"diff:",pentagons[j+i]-pentagons[j]
         end = True
         break
   if end : break


