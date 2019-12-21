a=input().split()
times=[int(n) for n in a]
numbers=[(times[0]*30+times[1]/2+times[2]/120)%360, (times[1]*6+times[2]/10)%360, (times[2]*6)%360]
numbers.sort(key=float)
t1=times[3]*30
t2=times[4]*30
def reg(x):
	if numbers[0]<x<numbers[1]:
		return 1
	if numbers[1]<x<numbers[2]:
		return 2
	else:
		return 3

if reg(t1)==reg(t2):
	print("YES")
else:
	print("NO")
