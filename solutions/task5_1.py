input()
arr = tuple(map(int, input().split()))
i_best = j_best = i_min = 0

for i in range(2, len(arr)):
    if arr[i - 1] < arr[i_min]:
        i_min = i - 1
    if 1 < (arr[i] / arr[i_min]) > (arr[j_best] / arr[i_best]):
        i_best, j_best = i_min, i

print(i_best + 1 if i_best else 0, j_best + 1 if j_best else 0)
