# Next Round
a = input()
b = input()
a1 = a.split()
b1 = b.split()
list1 = []
for i in b1:
    if int(i) >= int(b1[int(a1[1]) - 1]) and int(i) > 0:
        list1.append(i)

print(len(list1))
