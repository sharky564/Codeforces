# Tram
a = int(input())
inputs = [input() for i in range(a)]

min_cap = 0
num = 0
for i in inputs:
    c = i.split()
    num += int(c[1]) - int(c[0])
    if num > min_cap:
        min_cap = num

print(min_cap)
