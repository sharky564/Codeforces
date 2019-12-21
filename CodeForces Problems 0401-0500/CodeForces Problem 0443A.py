a=input()
b=list(a)
invalid=['{',',',' ','}']
valid=[]
for i in b:
  if i not in invalid:
    valid.append(i)
count=len(set(valid))
print(count)
