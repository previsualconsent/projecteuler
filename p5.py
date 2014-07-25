import math
import Prime

lcm = Prime.factor(2)
for i in range(3,21):
   lcm  = lcm.LCM(Prime.factor(i))
   print reduce(lambda x, y: x*y, lcm.getlist())




