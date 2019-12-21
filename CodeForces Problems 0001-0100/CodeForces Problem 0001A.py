# Theatre Square
from math import ceil


def p(n, m, a):
    return ceil(n / a) * ceil(m / a)


x = input()
y = x.split()
print(p(int(y[0]), int(y[1]), int(y[2])))
