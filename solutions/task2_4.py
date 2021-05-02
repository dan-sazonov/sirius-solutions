n = int(input())
steps = [0] * (n + 1)

for i in range(2, n + 1):
    steps[i] = steps[i - 1]

    if i % 2 == 0 and steps[i // 2] < steps[i]:
        steps[i] = steps[i // 2]

    if i % 3 == 0 and steps[i // 3] < steps[i]:
        steps[i] = steps[i // 3]

    steps[i] += 1

print(steps[n])
