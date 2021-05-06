from bisect import bisect_right


def ok(x, b, k):
    s = x
    j = 0
    for i in range(k):
        j = bisect_right(b, s, j)
        s = b[j - 1] + x
    if s - x >= b[-1]:
        return True
    return False


n = int(input())
a = [int(i) for i in input().split()]
k = int(input())

for i in range(1, n):
    a[i] += a[i - 1]
l = 0
r = a[-1]

while r - l > 1:
    x = (r + l) // 2
    if ok(x, a, k):
        r = x
    else:
        l = x

print(r)
