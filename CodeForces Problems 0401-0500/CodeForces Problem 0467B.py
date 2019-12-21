a=input().split()

n=int(a[0])
m=int(a[1])
k=int(a[2])

x=[int(input()) for i in range(m)]

Fedor=int(input())

orig_Fedor_bin=str(bin(Fedor)).replace('0b','')

total=0

for i in x:
	orig_x_bin=str(bin(i)).replace('0b','')
	x_bin=list(orig_x_bin.zfill(max(len(orig_Fedor_bin),len(orig_x_bin))))
	Fedor_bin=list(orig_Fedor_bin.zfill(max(len(orig_Fedor_bin),len(orig_x_bin))))
	j=0
	t=min(len(Fedor_bin),len(x_bin))
	rev_Fedor_bin=Fedor_bin[::-1]
	rev_x_bin=x_bin[::-1]
	count=abs(len(Fedor_bin)-len(x_bin))
	while j<t:
		if rev_Fedor_bin[j]!=rev_x_bin[j]:
			count+=1
		j+=1
	else:
		if count<=k:
			total+=1

print(total)
