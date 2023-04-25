def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)
  
def gcd_ext(a, b):
  if b == 0:
      return a, 1, 0
  d, x, y = gcd_ext(b, a % b)
  x, y = y, x - (a // b) * y
  return d, x, y 
  
def main():  
  a, b, c = map(int, input().split())
  d, x, y = gcd_ext(a, b)
  if c % d != 0:
    print(-1)
  else:
    t = (x * (c // d)) // int(b / d)
    xres = (c // d) * x - (b // d) * t
    yres = (c // d) * y + (a // d) * t
    print(xres, yres)
    
if __name__ == "__main__":
    main()  
