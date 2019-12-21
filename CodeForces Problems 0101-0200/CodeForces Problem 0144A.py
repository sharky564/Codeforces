# Arrival of the General
a=int(input())
b=input()
c=b.split()
d = []
count=0
for i in c:
    d.append(int(i))
max = d.index(max(d))
count+=max
newlist=[d[max]]
for i in d[:max]:
  newlist.append(i)
for i in d[max+1:]:
  newlist.append(i)
min = min(newlist)
e = [i for i, j in enumerate(newlist) if j == min]
count+=a-e[-1]-1
print(count)
