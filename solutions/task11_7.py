from bisect import *

n = int(input())
a = []
s = 0

for _ in range(n):
    a.append(int(input()))
a.sort()

for i in range(n - 1):
    for j in range(i + 1, n):
        min_ = abs(a[i] - a[j])
        max_ = (a[i] + a[j])
        ri = bisect_right(a, min_)
        ra = bisect_right(a, max_)
        while ra > 0 and a[ra - 1] == max_:
            ra -= 1
        if ri <= j:
            ri = j + 1
        if ra <= j:
            ra = j + 1
        s += (ra - ri)

print(s)
