a=input()
b=input()
c=a.split()
d=b.split()
bent=0
for i in d:
	if int(i)>int(c[1]):
		bent+=1
print(bent+int(c[0]))
