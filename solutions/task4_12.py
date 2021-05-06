from math import factorial, sqrt


def factor(n):
    res = []
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            res.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        res.append(n)
    return res


n = int(input())
if n == 1:
    print(1)
else:
    primes = factor(factorial(n))
    ans, num, current, = 1, 1, primes[0]
    for j in range(1, len(primes)):
        if primes[j] == current:
            num += 1
        else:
            ans *= num + 1
            num = 1
            current = primes[j]
    print(ans * (num + 1))
