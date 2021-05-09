n = int(input())
a = sorted(map(int, input().split()))

if n == 2:
    print(abs(a[1] - a[0]))
    exit(0)

ans = [0, a[1] - a[0], a[2] - a[0]]
for i in range(3, n):
    tmp = min(ans[i - 1], ans[i - 2]) + a[i] - a[i - 1]
    ans.append(tmp)

print(ans[-1])
