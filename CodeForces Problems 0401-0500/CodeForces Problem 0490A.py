a=int(input())
b=input().split()
k=min(b.count('1'), b.count('2'), b.count('3'))
print(k)
list1=[]
list2=[]
list3=[]
i=0
while i<a:
	if b[i]=='1':
		list1.append(i)
	elif b[i]=='2':
		list2.append(i)
	else:
		list3.append(i)
	i+=1

while k>0:
	team=[str(list1[0]+1),str(list2[0]+1),str(list3[0]+1)]
	del list1[0]
	del list2[0]
	del list3[0]
	print(' '.join(team))
	k-=1
