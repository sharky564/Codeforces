# Word
a = input()
b = a.lower()
c = list(a)
d = list(b)
lower = 0
i = 0
while i < len(c):
    if c[i] == d[i]:
        lower += 1
    i += 1

if 2 * lower >= len(c):
    print(a.lower())
else:
    print(a.upper())
