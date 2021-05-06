n = int(input())
arr = list(map(int, input().split()))


def merge(left, right):
    res = []
    count = 0
    l_index, r_index = 0, 0

    while count < len(left) + len(right):
        if l_index < len(left) and r_index < len(right):
            if left[l_index] <= right[r_index]:
                res.append(left[l_index])
                l_index += 1
            else:
                res.append(right[r_index])
                r_index += 1

        elif l_index == len(left):
            res.append(right[r_index])
            r_index += 1
        elif r_index == len(right):
            res.append(left[l_index])
            l_index += 1
        count += 1
    return res


def m_s(nums):
    half = len(nums) // 2
    if len(nums) > 1:
        return merge(m_s(nums[:half]), m_s(nums[half:]))
    return nums


print(' '.join(map(str, m_s(arr))))
