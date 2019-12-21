from math import ceil
a=input().split()
n=int(a[0])
m=int(a[1])
if n<m:
	print('-1')
else:
	print(m*ceil(ceil(n/2)/m))
