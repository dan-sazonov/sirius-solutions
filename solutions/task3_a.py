n = int(input())
m = 0
f = 1

for i in range(1, n + 1):
    x = i
    while x % 2 == 0:
        x //= 2
        m += 1
    while x % 5 == 0:
        x //= 5
        m -= 1
    f = f * x % 10
for i in range(m):
    f = f * 2 % 10

print(f)
