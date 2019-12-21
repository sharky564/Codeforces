a=int(input())
b=input().split()
max=0
i=0
while i<a:
	j=i
	while j<a:
		list1=[]
		list2=[]
		list3=[]
		for k1 in range(0,i):
			list1.append(b[k1])
		for k2 in range(i,j+1):
			list2.append(b[k2])
		for k3 in range(j+1,a):
			list3.append(b[k3])
		if max<list1.count('1')+list2.count('0')+list3.count('1'):
			max=list1.count('1')+list2.count('0')+list3.count('1')
		j+=1
	i+=1

print(max)
