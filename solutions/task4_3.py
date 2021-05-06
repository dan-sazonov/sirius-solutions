from math import sqrt

n = int(input())
sigma_0 = sigma_1 = 0

for i in range(1, int(sqrt(n)) + 1):
    if not n % i and i != sqrt(n):
        sigma_0 += 2
        sigma_1 += i + n // i
    elif not n % i and i == sqrt(n):
        sigma_0 += 1
        sigma_1 += i

print(sigma_0, sigma_1)
