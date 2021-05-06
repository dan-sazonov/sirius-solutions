from math import fabs

NN = 1000000
eps = 1e-7
h = [0 for _ in range(NN)]


def get_h():
    global a, h, s
    assert (s < t)
    return a[h[s]]


def pop_h():
    global s, h
    assert (s < t)
    s += 1
    return h[s - 1]


def push_h(x):
    global t, h, s, a
    while s < t and a[h[t - 1]] < a[x]:
        t -= 1
    h[t] = x
    t += 1


n, C = str(input()).split()
n = int(n)
C = float(C)
a = [0 for _ in range(NN)]
for i in range(n - 1):
    a[i] = int(input())
p = [0 for i in range(n)]
s = 0
t = 0
i = 0
j = 1
l = C
r = 0
push_h(0)

while i < j < n and l > (a[j - 1] + eps):
    ev1 = (l - r) * (j - i) / (j - i + 1)
    if s < t:
        ev2 = (l - get_h()) * (j - i)
        ev = min(ev2, ev1)
    else:
        ev = ev1
    l -= (ev / (j - i))
    r += ev
    if fabs(l - r) < eps:
        push_h(j)
        j += 1
        r = 0
    if fabs(l - get_h()) < eps:
        x = pop_h()
        while i <= x:
            p[i] = l
            i += 1
        i = x + 1
    if (i == j) or (l < a[j - 1] + eps):
        while i < j:
            p[i] = l
            i += 1
        l = r
        r = 0
        i = j
        push_h(j)
        j += 1

while i < j:
    p[i] = l
    i += 1

for i in range(n):
    print(p[i])
