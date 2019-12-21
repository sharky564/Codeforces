a=input().split()
n=int(a[0])
x=int(a[1])
count=0
for i in range(1,min(x+1,n+1)):
	if x%i==0 and x//i <= n:
		count+=1

print(count)
