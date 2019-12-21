# Fancy Fence
from math import floor
t=int(input())
angles=[int(input()) for i in range(t)]
for i in angles:
	if 360/(180-i)==floor(360/(180-i)):
		print("YES")
	else:
		print("NO")
