
import sys
from time import time
from subprocess import call


f = open("README.md","w")
f.write("## Times for Each Problem\n\n")
for i in range(1, int(sys.argv[1])+1):
   t = time()
   call(["python2", "p%03d.py"%i])
   f.write("%i.  %.3f seconds\n" %(i, time()-t))

f.close()
   
