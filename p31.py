
def makeChange(n,coins):
   ''' Generater that produces a sequence of coin stacks from [coins] summing to n '''
   notDone = True
   combos = 0
   i = 0
   stack = []
   while notDone:
      while sum(stack) < n:
         stack.append(coins[i])
      else:
         if sum(stack) == n:
            yield stack
            combos += 1
            if not combos % 10000:
               print combos, stack
         p = stack.pop()
         while p == coins[-1]:
            if len(stack) == 0:
               notDone = False
               break
            else:
               p = stack.pop()
         else:
            i = coins.index(p)
         i += 1
   

coins = [200, 100, 50, 20, 10, 5, 2, 1]
n = 200
print len([i for i in makeChange(n,coins)])


