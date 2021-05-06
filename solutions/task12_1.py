w, h, n = map(int, input().split())
L = max(w, h)
R = L * n

while R - L > 1:
    M = (R + L) // 2
    res = (M // w) * (M // h)
    if res < n:
        L = M
    else:
        R = M

print(R)
