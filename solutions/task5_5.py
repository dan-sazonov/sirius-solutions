n, m = map(int, input().split(maxsplit=1))
p = [0]
h = None

for i in map(int, input().split(maxsplit=n - 1)):
    if not (h is None):
        p.append(p[-1] + (i > h))
    h = i

for _ in range(m):
    l, m = map(int, input().split(maxsplit=1))
    print(p[m - 1] - p[l - 1])
