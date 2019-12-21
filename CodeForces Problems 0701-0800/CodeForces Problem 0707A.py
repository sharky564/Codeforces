a=input().split()
b=[input().split() for i in range(int(a[0]))]
new_b=[j for i in b for j in i]
newer_b=set(new_b)
colour={'C', 'M', 'Y'}
i=0
while i<len(newer_b):
	if list(newer_b)[i] in colour:
		print("#Color")
		break
	else:
		i+=1
else:
	print("#Black&White")
