from math import floor
from math import log
a=input().split()
l=int(a[0])
b=int(a[1])
print(floor(log(b/l,1.5))+1)
