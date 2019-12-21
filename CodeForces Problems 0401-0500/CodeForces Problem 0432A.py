a=input()
b=input()
a1=a.split()
b1=b.split()
c=0
for i in b1:
	if int(i)+int(a1[1])<=5:
		c+=1

print(c//3)
