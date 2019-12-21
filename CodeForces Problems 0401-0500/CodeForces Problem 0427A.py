a=int(input())
b=input().split()
sum=0
count=0
for j in b:
	i=int(j)
	if i<0:
		sum+=i
		if sum < 0:
			count+=1
	else:
		if sum<0:
			sum=i
		else:
			sum+=i

print(count)
