# Presents

a=input()
b=input()
c=b.split()
c.sort(key=float)
d=b.split()

list1=[]
x=1
while x<=len(d):
  list1.append(c[d.index(str(x))])
  x+=1

print(''.join(list1))
