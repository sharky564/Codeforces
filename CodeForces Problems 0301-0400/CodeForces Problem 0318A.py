from math import ceil
a=input()
b=a.split()
if int(b[1])<= ceil(int(b[0])/2):
	print(int(b[1])*2-1)

else:
	print((int(b[1])-ceil(int(b[0])/2))*2)
