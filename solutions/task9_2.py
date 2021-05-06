n, c = int(input()), tuple(map(int, input().split()))
k, p = int(input()), tuple(map(int, input().split()))
arr = [0] * n

for i in range(k):
    arr[p[i] - 1] += 1
for j in range(n):
    print('yes' if arr[j] > c[j] else 'no')
