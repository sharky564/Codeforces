a=input()
b=input()
c=a.split()
d=b.split()

room=1
while room<int(c[1]):
    room+=int(d[room-1])

if room==int(c[1]):
    print('YES')
else:
    print('NO')
