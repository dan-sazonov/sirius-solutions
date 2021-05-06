from math import ceil

n = int(input())
h = list(map(int, input().split()))
m = int(input())
l = 0
r = max(h)

while r - l > 1:
    x = (r + l) // 2
    if sum(list(map(lambda a: ceil(a / x), h))) <= m:
        r = x
    else:
        l = x

if m < n:
    print(-1)
else:
    print(r)
