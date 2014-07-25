
import sys
from time import time
from subprocess import call


f = open("README.md","w")
for i in range(1, int(sys.argv[1])+1):
   t = time()
   call(["python", "p%i.py"%i])
   f.write("Problem %i: %.3f seconds\n" %(i, time()-t))

f.close()
   
