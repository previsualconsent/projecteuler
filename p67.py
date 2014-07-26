
f = open("p67tri.txt","r")

tri = []
for line in f:
   tri.append( [ int(i) for i in line.split(' ') ] )


for j in range(len(tri)-1,-1,-1):
   for i in range(len(tri[j])-1):
      tri[j-1][i] += max(tri[j][i],tri[j][i+1])
   
print tri[0][0]


   

