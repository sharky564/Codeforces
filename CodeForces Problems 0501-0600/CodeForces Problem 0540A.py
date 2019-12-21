a=int(input())
b=list(input())
c=list(input())

i=0
count=0
while i<a:
	if abs(int(b[i])-int(c[i]))<=5:
		count+=abs(int(b[i])-int(c[i]))
	else:
		count+=10-abs((int(b[i])-int(c[i])))
	i+=1

print(count)
