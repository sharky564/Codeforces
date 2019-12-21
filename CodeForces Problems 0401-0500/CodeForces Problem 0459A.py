# Pashmak and Garden
coords = input().split()
x1 = int(coords[0])
y1 = int(coords[1])
x2 = int(coords[2])
y2 = int(coords[3])

if x1 == x2:
    s = abs(y1 - y2)
    x3 = s + x1
    y3 = y1
    x4 = s + x2
    y4 = y2
    print(x3, y3, x4, y4)
elif y1 == y2:
    s = abs(x1 - x2)
    x3 = x1
    y3 = s + y1
    x4 = x2
    y4 = s + y2
    print(x3, y3, x4, y4)
elif abs(x1 - x2) == abs(y1 - y2):
    x3 = x1
    y3 = y2
    x4 = x2
    y4 = y1
    print(x3, y3, x4, y4)
else:
    print(-1)
