a=input()
b=a.split()
k=1
while k<11:
	if (k*int(b[0]))%10==0 or (k*int(b[0]))%10==int(b[1]):
		break
	k+=1

print(k)
