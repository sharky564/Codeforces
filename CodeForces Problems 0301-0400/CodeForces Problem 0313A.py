a=input()
b=list(a)
b1=list(a)
b2=list(a)
del b1[len(b)-2]
del b2[len(b)-1]

c=int(a)
c1=''.join(b1)
c2=''.join(b2)
print(max(c,int(c1),int(c2)))
