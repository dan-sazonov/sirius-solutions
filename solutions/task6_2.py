inf = 2 * (10 ** 9) + 1
a = list(map(int, input().split()))
n = a[0]
h = [-inf] + a[1:] + [-inf]
ans = [[0, 0] for i in range(n + 2)]
stack = [0]

for i in range(1, n + 2):
    tmp = h[i]
    while h[stack[-1]] > tmp:
        ans[stack.pop()][1] = i
    stack.append(i)

stack = [0]
for i in range(n + 1, 0, -1):
    tmp = h[i]
    while h[stack[-1]] > tmp:
        ans[stack.pop()][0] = i
    stack.append(i)

m = -inf
for i in range(1, n + 1):
    s = h[i] * (ans[i][1] - ans[i][0] - 1)
    m = max(m, s)

print(m)
