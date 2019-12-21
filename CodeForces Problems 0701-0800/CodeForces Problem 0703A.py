a=int(input())
dice_results=[input() for i in range(a)]
mishka=0
chris=0
for i in dice_results:
	j=i.split()
	if int(j[0])>int(j[1]):
		mishka+=1
	elif int(j[0])<int(j[1]):
		chris+=1

if mishka > chris:
	print("Mishka")
elif mishka < chris:
	print("Chris")
else:
	print("Friendship is magic!^^")
