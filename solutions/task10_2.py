ans = []

for i in input():
    if i not in ans:
        ans.append(i)

print(*ans, sep='')
