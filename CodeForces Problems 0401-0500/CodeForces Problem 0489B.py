n=int(input())
b=input().split()
bskill=[int(i) for i in b]
m=int(input())
g=input().split()
gskill=[int(i) for i in g]
bskill.sort()
gskill.sort()

count=0
i=0
while i<len(bskill):
	s=bskill[i]
	k={s-1,s,s+1}
	j=0
	while j<len(gskill):
		if gskill[j] in k:
			count+=1
			del bskill[i]
			del gskill[j]
			break
		else:
			j+=1
	else:
		i+=1

print(count)
