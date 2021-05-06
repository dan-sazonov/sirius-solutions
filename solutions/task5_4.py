n, k, m = map(int, input().split())
a = list(map(int, input().split()))
res = 0

total = sum(a[:k + 1])
if total != m:
    for i in range(1, n - k):
        total += a[i + k] - a[i - 1]
        if total == m:
            res = i + 1
            break
else:
    res = 1

print(res)
