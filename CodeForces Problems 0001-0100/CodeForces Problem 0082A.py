# Double Cola
a = int(input())
i = 0
while 5 * (2 ** i - 1)<a:
    i += 1

shel = 5 * (2 ** (i) - 1) - 5 * 2 ** (i - 1) + 1
leon = 5 * (2 ** (i) - 1) - 4 * 2 ** (i - 1) + 1
penn = 5 * (2 ** (i) - 1) - 3 * 2 ** (i - 1) + 1
raje = 5 * (2 ** (i) - 1) - 2 * 2 ** (i - 1) + 1
howa = 5 * (2 ** (i) - 1) - 1 * 2 ** (i - 1) + 1
ends = 5 * (2 ** (i) - 1) + 1

if shel <= a < leon:
    print("Sheldon")
elif leon <= a < penn:
    print("Leonard")
elif penn <= a < raje:
    print("Penny")
elif raje <= a < howa
    print("Rajesh")
elif howa <= a < ends:
    print("Howard")
