n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
  a[i], b[i], c[i] = map(int, input().split())
  
g = [-1] * n
g[0] = a[0]

if n >= 2:
  g[1] = min(b[0], a[0] + a[1])
if n >= 3:
  g[2] = min(g[1] + a[2], g[0] + b[1], c[0], a[0] + a[1] + a[2])
  for i in range(3, n):
    g[i] = min(g[i - 1] + a[i], g[i - 2] + b[i - 1], g[i - 2] + a[i - 1] + a[i], g[i - 3] + c[i - 2], g[i - 3] + b[i - 2] + a[i], g[i - 3] + a[i - 2] + b[i - 1], g[i - 3] + a[i - 2] + a[i - 1] + a[i])
    
print(g[n - 1])
