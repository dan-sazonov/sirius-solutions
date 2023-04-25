def getsimple(n):
  g = {1: 0}
  n_tmp = n
  i = 2
  if n_tmp == 1:
    g[1] = 1
  else:
    while i <= int(n_tmp ** 0.5):
      count = 0
      while n_tmp % i == 0:
        count += 1
        n_tmp = n_tmp // i
      if count > 0:
        g[i] = count
      i += 1
    if n_tmp > 1:
      g[n_tmp] = 1
  return(g)

def main():
  a = int(input())
  imax = 1
  k = 1
  g_a = getsimple(a)

  for i in g_a.keys():
    k = k * i
    if g_a[i] > g_a[imax]:
      imax = i

  if k >= g_a[imax]:
    print(k)
  else:
    i_tmp = g_a[imax]
    for i in range(2, i_tmp):
      g_i = getsimple(k * i)
      bl = True
      for j in g_a.keys():
        if g_a[j] > g_i[j] * k * i:
          bl = False
          break
      if bl:
        k = k * i
        break
    print(k)

if __name__ == "__main__":
    main()      
