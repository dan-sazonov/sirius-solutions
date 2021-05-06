n = int(input())
data = list(map(int, input().split()))
data_prev = data.copy()

for i in range(n):
    j = i - 1
    key = data[i]
    while data[j] > key and j >= 0:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key
    if data != data_prev:
        print(*data)
    data_prev = data.copy()
