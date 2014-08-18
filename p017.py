

names = {
      1:"one",
      2:"two",
      3:"three",
      4:"four",
      5:"five",
      6:"six",
      7:"seven",
      8:"eight",
      9:"nine",
      10:"ten",
      11:"eleven",
      12:"twelve",
      13:"thirteen",
      14:"fourteen",
      15:"fifteen",
      16:"sixteen",
      17:"seventeen",
      18:"eighteen",
      19:"nineteen",
      20:"twenty",
      30:"thirty",
      40:"forty",
      50:"fifty",
      60:"sixty",
      70:"seventy",
      80:"eighty",
      90:"ninety"}


def int2string(n):
   global names
   if n in names:
      return names[n]
   nstr = str(n)
   string = ""
   needand = False
   for i,p in zip(nstr,range(len(nstr)-1,-1,-1)):
      i = int(i)
      if not i:
         continue
      if p == 3:
         string += names[i] + "thousand"
         needand = True
      elif  p == 2:
         string += names[i] + "hundred"
         needand = True
      elif p == 1:
         if needand:
            needand = False
            string += "and"
         if i>1:
            string += names[i*10]
         else :
            string += names[ int(nstr[-2:])]
            return string
      else:
         if needand:
            string += "and"
         return string + names[i]
   return string


allnums = ""
for i in range(1,1000+1):
   tmpstr = int2string(i)
   #print i,tmpstr
   allnums += tmpstr

print "total",len(allnums)

