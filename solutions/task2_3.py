n = int(input())
stairs = [0, 1, 2, 4]

if n <= 3:
    print(stairs[n])
    exit(0)

for i in range(n-3):
    stairs.append(sum(stairs[-3:]))

print(stairs[-1])
