n, x, y = map(int, input().split())
left, right = 0, (n - 1) * max(x, y)

while right > left + 1:
    middle = (right + left) // 2
    if (middle // x + middle // y) < n - 1:
        left = middle
    else:
        right = middle

print(right + min(x, y))
