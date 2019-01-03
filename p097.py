m = 28433
p = 7830457

modulo = 10000000000

result = 2
for i in range(p-1):
    result *= 2
    result = result % modulo

print (result*m +1) % modulo
