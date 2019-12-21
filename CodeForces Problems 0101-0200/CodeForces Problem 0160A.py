# Twins
a=input()
b=input()
min_coin=int(a)
c=b.split()
c.sort(key=float)
total_sum=0
for i in c:
  total_sum+=int(i)
sum=0
x=int(a)-1
count=0
while 2*sum<=total_sum:
  sum+=int(c[x])
  x-=1
  count+=1

print(count)
