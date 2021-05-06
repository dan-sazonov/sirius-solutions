_ = input()
nums = list(map(int, input().split()))
n = n_tmp = len(nums)
D = dict.fromkeys(nums, 0)
k = len(D)
cnt = 0
i, j = 0, 0
ans = (1, n)

while j < n:
    if cnt < k:
        if D[nums[j]] == 0:
            cnt += 1
        D[nums[j]] += 1
        j += 1
    else:
        D[nums[i]] -= 1
        if D[nums[i]] == 0:
            cnt -= 1
            if j - i < n_tmp:
                n_tmp = j - i
                ans = (i + 1, j)
        i += 1

while i < j and cnt == k:
    D[nums[i]] -= 1
    if D[nums[i]] == 0:
        if j - i < n_tmp:
            n_tmp = j - i
            ans = (i + 1, j)
        break
    i += 1

print(*ans)
