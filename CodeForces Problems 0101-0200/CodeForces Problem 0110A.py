# Nearly Lucky Number
a=input()
digits = ('4','7')
count=0
b=list(a)
for i in b:
  if i in digits:
    count+=1

c=list(str(count))
k=0
while k<len(c):
  if c[k] not in digits:
    print("NO")
    break
  else:
    k+=1
else:
  print("YES")
