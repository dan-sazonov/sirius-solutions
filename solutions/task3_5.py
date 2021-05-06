numbers = [[int(i) for i in input().split()] for _ in range(int(input()))]

for pair in numbers:
    x, y, z = pair[1], pair[0] - 2, pair[0]
    res = 1
    p = x % z
    while y:
        if y & 1:
            res = (res * p) % z
        y >>= 1
        p = (p * p) % z
    print(res)
