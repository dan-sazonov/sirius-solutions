from math import gcd

n = int(input())
pairs = []
i = amount = 0

while i ** 2 <= n:
    i += 1
    mod, div = n % i, n // i
    if not mod:
        pairs.extend([i, div])
pairs = sorted(list(set(pairs)))

for i in range(len(pairs) - 1):
    for j in range(i + 1, len(pairs)):
        if n < pairs[i] * pairs[j]:
            break
        elif gcd(pairs[i], pairs[j]) == 1:
            amount += 1

print(amount)
