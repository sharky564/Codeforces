a=input()
b=a.split()
c=240-int(b[1])
count=0
while c>=0:
	c-=(count+1)*5
	count+=1

print(min(int(b[0]),count-1))
