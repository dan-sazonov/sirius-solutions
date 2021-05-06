n = int(input())
arr = list(map(int, input().split()))
unordered = True
iter_counter = 0

while unordered:
    unordered = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]
            unordered = True
            iter_counter += 1
    n -= 1

print(iter_counter)
