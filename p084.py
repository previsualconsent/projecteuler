import numpy as np
import sys
spaces = [ "go", "a1", "cc1", "a2", "t1", "r1", "b1", "ch1", "b2", "b3",
   "jail", "c1", "u1", "c2", "c3", "r2", "d1", "cc2", "d2", "d3", "fp", "e1",
   "ch2", "e2", "e3", "r3", "f1", "f2", "u2", "f3", "g2j", "g1", "g2", "cc3",
   "g3", "r4", "ch3", "h1", "t2", "h2",]


twod6 = [0,0,1,2,3,4,5,6,5,4,3,2,1]
dN = 6
#twod4 = [0,0,1,2,3,4,3,2,1]
#dN = 4

dice = np.array([float(x)/sum(twod6) for x in twod6])
#dice = np.array([float(x)/sum(twod4) for x in twod4])

doubledoubles = (1./dN)**2
probjail = 0

#2d6 doubles
doubles = np.array([0,0, 1., 0, 1./3, 0, 1./5, 0, 1./5, 0, 1./3, 0, 1])
#2d4 doubles
#doubles = np.array([0,0, 1., 0, 1./3, 0, 1./3, 0, 1])
dice = dice * (1 - doubledoubles* doubles)

tripledouble = 1 - sum(dice)
#spaces = "abcedfg"
#dice = [.1, .2, .3, .4]

odds = np.zeros((len(spaces),len(spaces)))

for i in xrange(len(spaces)):
   if len(spaces) - i < len(dice):
      odds[i,i:] += dice[:len(spaces)-i]
      odds[i,:len(dice) - (len(spaces)-i)] += dice[-(len(dice) - (len(spaces)-i)):]
   else:
      odds[i,i:len(dice)+i] += dice
   odds[i,spaces.index("jail")] += tripledouble

# Set g2j odds
odds[:,spaces.index("jail")] += odds[:,spaces.index("g2j")]
odds[:,spaces.index("g2j")] = np.zeros(len(odds))


from copy import deepcopy
#chance
chance = {
      "ch1":["go", "jail", "c1", "e3", "h2", "r1", "r2", "r2", "u1", "h2"],
      "ch2":["go", "jail", "c1", "e3", "h2", "r1", "r3", "r3", "u2", "d3"],
      "ch3":["go", "jail", "c1", "e3", "h2", "r1", "r1", "r1", "u1", "cc3"],
      }
for ch in chance:
   chodds = deepcopy(odds[:,spaces.index(ch)])
   odds[:,spaces.index(ch)] = chodds*6./16
   for card in chance[ch]:
      odds[:,spaces.index(card)] += chodds*1./16
#community chest
cci = [spaces.index(cc) for cc in ["cc1","cc2","cc3"]]
for cc in cci:
   ccodds = deepcopy(odds[:,cc])
   odds[:,cc] = ccodds*14./16
   odds[:,spaces.index("go")] += ccodds*1./16
   odds[:,spaces.index("jail")] += ccodds*1./16

print "    ",
for space in spaces:
   print "%5s |" % space,
print
for i in range(len(odds)):
   print "----",
   for j in range(len(odds)):
      print "------|",
   print
   print "%4s" % spaces[i],
   for j in range(len(odds)):
      print "%5.2f%%|" %  (100*odds[i,j]),
   print
   
import sympy
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
sympy.init_printing(use_unicode=True)
ind = np.linspace(0,len(spaces),len(spaces))

M = sympy.Matrix(odds).T
V = sympy.Matrix(np.ones(len(odds)))
V[0] = 1
plotV =  np.array(V.T).astype(np.float64)[0]
bar = plt.bar(ind, plotV, .8)
plt.xticks(ind,spaces, rotation="vertical")
plt.show(block=False)
loop = True
while loop:
   newV=M*V
   diff = (newV - V).norm()
   if diff < .001:
      loop  = False
   V=newV
   plotV =  np.array(V.T).astype(np.float64)[0]
   for b,v in zip(bar,plotV):
      b.set_height(v)
   plt.ylim(min(plotV)*.9, max(plotV)*1.1)
   fig.canvas.draw_idle()
   try:
      fig.canvas.flush_events()
   except NotImplementedError:
      pass

plt.savefig("monopoly.png")
#print zip(V,spaces)
results = sorted( zip(V, spaces), reverse=True)

for prob,space in results[:3]:
   print space, spaces.index(space), prob/len(spaces)

