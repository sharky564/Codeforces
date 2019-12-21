# Devu, the Singer and Churu, the Joker
l1 = input().split()
n = int(l1[0])
d = int(l1[1])
t = [int(i) for i in input().split()]
if sum(t) + 10 * (n - 1) > d:
    print(- 1)
else:
    print(int((d - sum(t))/5))
