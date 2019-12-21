a=input()
b=a.split()
sum=0
for i in b:
	sum+=int(i)
if sum%5!=0 or sum==0:
	print(-1)
else:
	print(sum//5)
