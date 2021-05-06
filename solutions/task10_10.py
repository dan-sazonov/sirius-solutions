n = int(input())
castles = list()
x = set()
y = set()

for i in range(n):
    castles.append(list(map(int, input().split())))

castles.sort()
for i in range(n - 1):
    if castles[i + 1][0] == castles[i][0] and castles[i + 1][1] > castles[i][1]:
        y.add(castles[i][1] + 1)
    else:
        x.add(castles[i][0] + 1)

print(len(x) + len(y))
for i in y:
    print('y %d' % i)
for i in x:
    print('x %d' % i)
