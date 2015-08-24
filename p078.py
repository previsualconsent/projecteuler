from Tools import partitions,gen_pent

for i in xrange(100000):
   p = partitions(i)
   if not p % 1000000:
      print i,p
      break

