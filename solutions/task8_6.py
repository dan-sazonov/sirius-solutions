n, k = tuple(map(int, input().split()))
unordered = True
num = list(range(1, n + 1))
iter_counter = 0

while unordered and iter_counter < k:
    unordered = False
    for i in range(n - 1):
        if num[i] < num[i + 1] and iter_counter < k:
            num[i + 1], num[i] = num[i], num[i + 1]
            iter_counter += 1
            unordered = True

print(' '.join(map(str, num)))
