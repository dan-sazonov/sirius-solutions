def push(stack, elem):
    stack.append(elem)
    return elem


def top(stack):
    return stack[-1]


def pop(stack):
    return stack.pop()


def size(stack):
    return len(stack)


def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a, n // 2)
    else:
        return power(a, n - 1) * a


inf = 2 * power(10, 9) + 1
w, h = [-inf], [-inf]
n = int(input())

for i in range(n):
    wi, hi = map(int, input().split())
    w.append(wi)
    h.append(hi)
w.append(-inf)
h.append(-inf)

ans = [[0, 0] for i in range(n + 2)]
stack = []
push(stack, 0)

for i in range(1, n + 2):
    curr = h[i]
    while h[top(stack)] > curr:
        ans[pop(stack)][1] = i
    push(stack, i)

stack = []
push(stack, 0)
for i in range(n + 1, 0, -1):
    curr = h[i]
    while h[top(stack)] > curr:
        ans[pop(stack)][0] = i
    push(stack, i)

p = [0]
for i in range(1, n + 1):
    p.append(p[-1] + w[i])
p.append(p[-1])

m = -inf
for i in range(1, n + 1):
    li, ri = ans[i][0], ans[i][1]
    S = h[i] * (p[ri - 1] - p[li])
    m = max(m, S)

print(m)
