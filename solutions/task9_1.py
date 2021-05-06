s = input()
arr = [int(i) for i in s if i.isdigit()]
cnt = [0] * 10

for el in arr:
    cnt[el] += 1

arr = []
for i in range(len(cnt)):
    arr += [i] * cnt[i]

print(int(''.join(map(str, arr[::-1]))))
