a=int(input())
b=[input() for i in range(a)]
costs=[]
req=[]
for i in b:
	costs.append(int(i.split()[1]))
	req.append(int(i.split()[0]))
min_cost=costs[0]
total=0
i=0
while i<a:
	if min_cost<=costs[i]:
		total+=min_cost*req[i]
		i+=1
	else:
		min_cost=costs[i]
else:
	print(total)
