a=int(input())
b=input()
c=input()
d=b.split()
e=c.split()
d=d[1:]
e=e[1:]
levelx=[]
levely=[]
for i in d:
    if int(i)!=0:
        levelx.append(int(i))

for i in e:
    if int(i)!=0:
        levely.append(int(i))

leveltotal=levelx
for i in levely:
    leveltotal.append(i)

leveltotal=list(set(leveltotal))

all_levels=[]
for x in range(1,a+1):
    all_levels.append(x)

if all_levels==leveltotal:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
