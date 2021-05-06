from math import gcd

a, b, c, d = map(int, input().split())
x, y = abs(a - c), abs(b - d)
common = gcd(x, y)
print(common * (x // common + y // common - 1))
