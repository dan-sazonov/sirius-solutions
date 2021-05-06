n = int(input())
shirts = list(map(int, input().split()))
m = int(input())
trousers = list(map(int, input().split()))

s = 0
t = 0
sh = 0
tr = 0

while s < n and t < m:
    if abs(shirts[s] - trousers[t]) < abs(shirts[sh] - trousers[tr]):
        sh, tr = s, t

    if shirts[s] > trousers[t]:
        t += 1

    elif shirts[s] == trousers[t]:
        break

    else:
        s += 1

print(shirts[sh], trousers[tr])
