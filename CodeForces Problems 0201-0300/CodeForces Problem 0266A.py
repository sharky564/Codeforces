# Stones on the Table
a = input()
b = input()
c = list(b)
i = 0
count = 0
while i < len(c) - 1:
    if c[i] == c[i + 1]:
        c.remove(c[i + 1])
        count += 1
    else:
        i += 1

print(count)
