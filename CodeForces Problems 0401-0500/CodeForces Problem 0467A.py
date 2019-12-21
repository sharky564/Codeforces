a=int(input())
inputs=[]
n=0
while n<a:
    y=input()
    n+=1
    inputs.append(y)

count = 0
for i in inputs:
    b = i.split()
    if int(b[1])-int(b[0])>=2:
        count+=1

print(count)
