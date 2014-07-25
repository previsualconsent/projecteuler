
import sys
from time import time
from subprocess import call


f = open("README.md","w")
f.write("## Times for Each Problem\n\n")
for i in range(1, int(sys.argv[1])+1):
   t = time()
   call(["python", "p%i.py"%i])
   f.write("1.  %.3f seconds\n" %( time()-t))

f.close()
   
