n, r = map(int, input().split())
a = list(map(int, input().split()))

i, j, count = 0, 1, 0

while j < len(a) and i < len(a) - 1:
    if a[j] - a[i] <= r:
        j += 1
    else:
        count += n - j
        i += 1

print(count)
