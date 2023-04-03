n = int(input())
arr = list(map(int, input().split()))
p = [0] * (n + 1)
for i in range(1, n + 1):
  p[i] = p[i - 1] + arr[i - 1]

d = [-1] * 3
ibest = 0
jbest = 0
blen = 0
d[0] = 0

for j in range(1, n + 1):
  m = p[j] % 3
  if (d[m] == -1):
    d[m] = j
  else:
    if j - d[m] > blen:
      ibest = d[m] + 1
      jbest = j
      blen = j - d[m]
if blen == 0:
  print(-1)
else:
  print(ibest, jbest)
