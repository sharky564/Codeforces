# Game Shopping
temp = input().split()
c = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
count = 0
i = 0
while i < len(c) and len(a) > 0:
    if a[0] < c[i]:
        i += 1
    else:
        count += 1
        a = a[1:]
        c = c[i+1:]
        i = 0

print(count)
