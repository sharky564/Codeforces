# Dragons
import operator
a=input()
b=a.split()
inputs=[]
n=0
while n<int(b[1]):
    y=input()
    inputs.append(y)
    n+=1

dragonhp=[]
for i in inputs:
	j=i.split()
	dragonhp.append(j)

dragonhp.sort(key=lambda dragonhp:float(dragonhp[0]))
i=0
health=int(b[0])
while i<int(b[1]):
	j=dragonhp[i]
	if health<=int(j[0]):
		print('NO')
		break
	else:
		health+=int(j[1])
	i+=1
else:
	print('YES')
