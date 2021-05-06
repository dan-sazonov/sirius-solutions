from math import sqrt

c = float(input())
xo = sqrt(c)
eps = 1e-5
x = sqrt(c - xo)

while abs(x - xo) > eps:
    xo = x
    x = sqrt(c - sqrt(xo))

print(x)
