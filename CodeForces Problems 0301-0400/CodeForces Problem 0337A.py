a=input()
b=input()
c=a.split()
d=b.split()
d.sort(key=float)
i=0
min=int(d[len(d)-1])-int(d[0])
while i<=int(c[1])-int(c[0]):
    if int(d[i+int(c[0])-1])-int(d[i])<min:
        min=int(d[i+int(c[0])-1])-int(d[i])
    i+=1

print(min)
