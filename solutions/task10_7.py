n, m = map(int, input().split())
result = [0 for _ in range(n)]
ans = dict()
for _ in range(m):
    team, word = input().split()
    ans[word] = int(team)

for word in ans:
    result[ans[word] - 1] += 1

print(*result)
