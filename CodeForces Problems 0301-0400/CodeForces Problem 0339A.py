# Helpful Maths
a = input()
b = list(a)
numbers = ('1', '2', '3')
for i in b:
    if i == '+':
        b.remove(i)

c = sorted(b)
d = ''.join(c)
for i in numbers:
    if i in d:
        d = d.replace(i, i + '+')

print(d[:-1])
