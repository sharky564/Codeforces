a=int(input())
b=input().split()
c=[int(i) for i in b]
sum=0
k=max(c)
for i in c:
	if i!=k:
		sum+=k-i

print(sum)
