a=input()
b=input()
c=a.split()
d=b.split()
count=int(d[0])-1
i=1
while i<int(c[1]):
    count+=(int(d[i])-int(d[i-1]))%int(c[0])
    i+=1

print(count)
