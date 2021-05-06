from math import gcd

a, b = map(int, input().split())

divisor = gcd(a, b)
print(a // divisor, b // divisor)
