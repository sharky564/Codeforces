# I love \%username\%
a=int(input())
b=input()
c=b.split()
i=1
min=int(c[0])
max=int(c[0])
amazing=0
while i<a:
    if int(c[i])>max:
        amazing+=1
        max=int(c[i])
    elif int(c[i])<min:
        amazing+=1
        min=int(c[i])
    i+=1
print(amazing)
