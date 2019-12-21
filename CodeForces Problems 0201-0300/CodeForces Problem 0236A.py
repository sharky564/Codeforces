# Boy or Girl
a=input()
b=list(a)
letters=[]
for i in b:
  letters.append(i)
letters=set(letters)
if len(letters)%2==0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
