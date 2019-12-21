a=input()
b=input()
a1=a.split()
b1=b.split()
b1.sort(key=float)
d=max(int(b1[0]),int(a1[1])-int(b1[int(a1[0])-1]))
i=0
while i<int(a1[0])-1:
    if int(b1[i+1])-int(b1[i])>2*d:
        d=(int(b1[i+1])-int(b1[i]))/2
    i+=1
print(d)
