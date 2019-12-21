from math import ceil
a=input().split()
b=input().split()
n=int(input())
if ceil((int(a[0])+int(a[1])+int(a[2]))/5)+ceil((int(b[0])+int(b[1])+int(b[2]))/10) > n:
	print('NO')
else:
	print('YES')
