import string

alpha = dict(zip(string.ascii_uppercase,range(1,27)))

def alpha_value(name):
   ret = 0
   for l in name:
      ret += alpha[l]
   return ret

f = open("names.txt","r")

names = [name.strip("\" ") for name in f.readline().split(',')]
names.sort()

print sum( [ alpha_value(names[i])*(i+1) for i in range(len(names))])
