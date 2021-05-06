n = int(input()) + 2
a = [-1, *map(int, input().split()), -1]
ans = [0] * n
stack = [0]

for i in range(1, n):
    while a[stack[-1]] > a[i]:
        ans[stack.pop()] = i
    stack.append(i if i < n - 2 else -1)

print(*map(lambda x: x - 1, ans[1:-1]))
