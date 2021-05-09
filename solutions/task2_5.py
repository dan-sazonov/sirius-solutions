n, k = map(int, input().split())
ans = [[0, 0], [1, k - 1]]

for i in range(2, n + 1):
    dp_0 = ans[i - 1][1]
    dp_1 = (k - 1) * (ans[i - 1][0] + ans[i - 1][1])
    ans.append([dp_0, dp_1])

print(sum(ans[-1]))
