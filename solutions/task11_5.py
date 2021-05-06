def binary_search(listt, item):
    low = 0
    high = len(listt) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = listt[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


n, k = map(int, input().split())
lstn = list(map(int, input().split()))
lstk = list(map(int, input().split()))
for ans in lstk:
    if binary_search(lstn, ans) is None:
        print('NO')
    else:
        print('YES')
