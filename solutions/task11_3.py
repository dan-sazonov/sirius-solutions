n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in b:
    L = 0
    R = n - 1
    while R - L > 1:
        M = (R + L) // 2
        if a[M] < i:
            L = M
        else:
            R = M
    if i - a[L] <= a[R] - i:
        print(a[L])
    else:
        print(a[R])
