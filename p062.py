
from Tools import is_perm
max_n =  100000

cubes = [ i**3 for i in xrange(max_n) ] 
cube_perms = []
icube_perms = []
checked = [ False for i in xrange(max_n) ]

for i in xrange(max_n):
   if checked[i]:
      continue
   for j in xrange(i+1,max_n):
      if len(str(cubes[j])) > len(str(cubes[i])):
         break
      if checked[j]:
         continue
      if is_perm(cubes[i],cubes[j]):
         cube_perms.append(cubes[j])
         icube_perms.append(j)
   if len(cube_perms) == 4:
      print cubes[i], cube_perms
      break
   checked[i] = True
   for j in icube_perms:
      checked[j] = True
   cube_perms = []
   icube_perms = []




