n = int(input())
a = list(map(int, input().split()))
left = [0 for _ in range(n)]
right = [0 for _ in range(n)]
s = [-1]

for i in range(n - 1, -1, -1):
    while s[-1] != -1 and a[s[-1]] > a[i]:
        s.pop()
    if s[-1] == -1:
        right[i] = a[i] * (n - i)
    else:
        right[i] = right[s[-1]] + a[i] * (s[-1] - i)
    s.append(i)
s = [-1]

for i in range(n):
    while s[-1] != -1 and a[s[-1]] > a[i]:
        s.pop()
    if s[-1] == -1:
        left[i] = a[i] * (i + 1)
    else:
        left[i] = left[s[-1]] + a[i] * (i - s[-1])
    s.append(i)

m = 0
ind = -1
for i in range(n):
    total = left[i] + right[i] - a[i]
    if total > m:
        m = total
        ind = i

i = ind - 1
j = ind + 1
m1 = a[ind]
m2 = a[ind]

while i >= 0:
    if a[i] > m1:
        a[i] = m1
    else:
        m1 = a[i]
    i -= 1

while j < n:
    if a[j] > m2:
        a[j] = m2
    else:
        m2 = a[j]
    j += 1

print(*a)
