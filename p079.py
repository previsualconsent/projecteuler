from collections import defaultdict
import random
import bisect

def insert(l, x):
   if x not in l:
      bisect.insort(l, x)
#code_len = 7
#n_logins = 50
#login_len = 3
#code = "".join([str(random.randint(0,9)) for i in range(code_len)])
#data = []
#for ilogin in range(n_logins):
#   login = [code[i] for i in sorted(random.sample(range(len(code)), login_len))]
#   data.append("".join(login))

#print code, data
with open("p079_keylog.txt","r") as f:
   data = []
   for line in f:
      data.append(line.strip())

keys = set("".join(data))
before = {}
#after = {}
for k in keys:
   before[k] = []
   #after[k] = []

for t in data:
   #insert(after [t[0]], t[1])
   #insert(after [t[0]], t[2])
   insert(before[t[1]], t[0])
   #insert(after [t[1]], t[2])
   insert(before[t[2]], t[0])
   insert(before[t[2]], t[1])

result = ""
for n,b in sorted(zip(map(len, before.values()),before)):
   result += str(b)
print result
