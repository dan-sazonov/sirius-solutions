n = int(input())
result = n
i = 1

while n + 1 > i ** 2:
    i += 1
    if not n % i:
        while not n % i:
            n //= i
        result -= result // i
        continue

print(result if n <= 1 else result - (result // n))
