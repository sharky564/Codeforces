a=int(input())
n=0
inputs=[]
while n<a:
	y=input()
	inputs.append(y)
	n+=1

i=0
while i<a:
	if 'OO' in inputs[i]:
		inputs[i]=inputs[i].replace('OO','++',1)
		print('YES')
		for row in inputs:
			print(''.join(row))
		break
	i+=1
else:
	print('NO')
