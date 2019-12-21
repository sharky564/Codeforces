a=int(input())
inputs=[]
n=0
while n<a:
    y=input()
    n+=1
    inputs.append(y)

i=0
count=1
while i<a-1:
    b=list(inputs[i])
    c=list(inputs[i+1])
    if b[1]==c[0]:
        count+=1
    i+=1

print(count)
