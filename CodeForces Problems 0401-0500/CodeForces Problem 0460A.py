a=input()
b=a.split()
count=int(b[0])-1
i=1
while count>0:
    count-=1
    i+=1
    if i%int(b[1])==0:
        count+=1

print(i)
