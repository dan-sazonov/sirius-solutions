n = int(input())
a = list(map(int, input().split()))
ans = [0, a[0]]

for i in range(2, n + 1):
    ans.append(max(ans[i - 1], ans[i - 2]) + a[i - 1])

print(ans[-1])
