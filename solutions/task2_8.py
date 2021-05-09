n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())

ans = [0, a[0], min(a[0] + a[1], b[0])]

for j in range(3, n + 1):
    tmp = min(ans[j - 1] + a[j - 1], ans[j - 2] + b[j - 2])
    ans.append(min(tmp, ans[j - 3] + c[j - 3]))

print(ans[-1])
