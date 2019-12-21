# IQ test
a = int(input())
b = input()
c = b.split()
x = int(c[0]) % 2
y = int(c[1]) % 2
z = int(c[2]) % 2
if x == y:
    i = 2
    while i < a:
        if int(c[i]) %2 != x:
            print(i + 1)
            break
        i += 1
else:
    if y == z:
        print(1)
    else:
        print(2)
