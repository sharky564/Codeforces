import numpy
n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
q=[int(i) for i in input().split()]

sums=numpy.cumsum(a)

i=0
while i<m:
	temp=[i for i in sums]
	temp.append(q[i])
	temp.sort()
	print(temp.index(q[i])+1)
	i+=1
