from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
perspective = deque()

for i in range(n):
    if i >= k and perspective[0] == i - k:
        perspective.popleft()
    while len(perspective) and arr[perspective[-1]] >= arr[i]:
        perspective.pop()
    perspective.append(i)
    if i >= k - 1:
        print(arr[perspective[0]])
