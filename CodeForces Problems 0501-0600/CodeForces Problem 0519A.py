a=[input() for i in range(8)]
white=0
black=0
for i in a:
	white+=i.count('Q')*9+i.count('R')*5+i.count('B')*3+i.count('N')*3+i.count('P')
	black+=i.count('q')*9+i.count('r')*5+i.count('b')*3+i.count('n')*3+i.count('p')
if white>black:
	print("White")
elif white<black:
	print("Black")
else:
	print("Draw")
