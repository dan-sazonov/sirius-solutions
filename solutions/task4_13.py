a, b = map(int, input().split())

numbers = [0, 0] + list(range(2, b + 1))
primes = []

i = 2
while i <= b:
    if numbers[i] != 0:
        primes.append(numbers[i])
        for j in range(i, b + 1, i):
            numbers[j] = 0
    i += 1

super_numbers = []
for j in range(len(primes)):
    for c in range(len(primes) - 1):
        g = primes[j] + primes[c]
        if a <= g <= b:
            super_numbers.append(g)

print(*sorted(list(set(super_numbers))), sep='\n')
