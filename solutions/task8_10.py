def compare(a, b):
    if a[1] == b[1]:
        return a[0] < b[0]
    else:
        return a[1] > b[1]


res = []
n = int(input())

for _ in range(n):
    arr = [int(s) for s in input().split()]
    res.append(arr)
for i in range(1, len(res)):
    tmp = res[i]
    j = i - 1
    while j >= 0 and compare(tmp, res[j]):
        res[j + 1] = res[j]
        j -= 1
    res[j + 1] = tmp
for c in res:
    print(*c)
