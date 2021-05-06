x = int(input())
a, b, = [0, 1, 4], []

for i in range(x):
    a.append(i ** 2)
    b.append(i ** 3)

print(sorted(list(set(a + b)))[x])
