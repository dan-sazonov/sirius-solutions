from math import gcd

n = int(input())
a = list(map(int, input().split()))
amount = 0

for i in range(n):
    if amount > n - i:
        break
    item = a[i]
    ans = 0

    for j in range(i, n):
        ans += 1
        item = gcd(a[j], item)
        if item == 1:
            break
        a[j] //= item
        amount = ans if ans > amount else amount

print(amount)
