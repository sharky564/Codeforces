a=input()
b=a.split()
n=str(10**(int(b[0])-1)+int(b[1])-(10**(int(b[0])-1)%(int(b[1]))))
if len(n)!=int(b[0]):
	print('-1')
else:
	print(n)
