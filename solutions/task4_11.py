from math import sqrt


def solve(n):
    j = 0
    while not (n & 1):
        j += 1
        n //= 2

    a = [2] * j
    a[-1] *= n

    if j == 1:
        print('prime')
        return None

    for i in range(3, int(sqrt(n)) + 1, 2):
        if not (n % i):
            b = a[:]
            b[-1] //= i
            b[-2] *= i
            print('many')
            print(' '.join(map(str, a)))
            print(' '.join(map(str, b)))
            return None

    print('single')
    print(' '.join(map(str, a)))


solve(int(input()))
