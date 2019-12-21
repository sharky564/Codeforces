# Ultra-Fast Mathematician
a = input()
b = input()
c = list(a)
d = list(b)
strlist = []
i = 0
while i < len(c):
    if c[i] == d[i]:
        strlist.append('0')
    else:
        strlist.append('1')
    i+=1

print(''.join(strlist))
