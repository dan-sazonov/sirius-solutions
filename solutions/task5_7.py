n = int(input())
a = []

while True:
    for i in range(n):
        a.append(int(input()))
    if n == 2:
        print(1, 2, sep='\n')
        break
    ans = a[0]
    ans_l = ans_r = s = 0
    minus_pos = -1
    for j in range(n):
        s += a[j]
        if s > ans:
            ans = s
            ans_l = minus_pos + 1
            ans_r = j
        if s <= 0:
            s = 0
            minus_pos = j
    print(ans_l + 1, ans_r + 1, sep='\n')
    break
