import Prime


Prime.prime_seive(100000)
triangle = 1
i = 1
while Prime.factor(triangle).getNdivisors() < 500:
   i += 1
   triangle += i

print triangle

