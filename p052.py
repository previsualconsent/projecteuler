

def are_permutation(n_list):
   a = sorted(str(n_list[0]))
   for b in n_list[1:]:
      if not a == sorted(str(b)):
         return False
   return True

done = False
n = 0
while not done:
   n+=1
   done = are_permutation([n*i for i in range(1,7)])

print [n*i for i in range(1,7)]
   

