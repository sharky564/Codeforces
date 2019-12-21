# Games
a=int(input())
inputs=[]
n=0
while n<a:
    y=input()
    n+=1
    inputs.append(y)

count=0
for i in inputs:
    b=i.split()
    inputs1= [k for k in inputs if k!=i]
    for j in inputs1:
        c=j.split()
        if b[0]==c[1]:
            count+=1

print(count)
