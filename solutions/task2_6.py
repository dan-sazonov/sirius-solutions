n = int(input())
ans = [0] * (n + 1)
ans[0] = 1
ans[1] = 2

if n < 2:
    print(ans[n])
else:
    ans[2] = 4
    for i in range(3, n + 1):
        ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]

    print(ans[-1])
