def gcd(a, b):
    if not a:
        return b, 0, 1
    div, x1, y1 = gcd(b % a, a)
    y = y1 - (b // a) * x1
    return div, y, x1


m, a = map(int, input().split())

gcd, x, _ = gcd(a, m)
number = (x % m + m) % m

print(number if gcd == 1 else -1)
