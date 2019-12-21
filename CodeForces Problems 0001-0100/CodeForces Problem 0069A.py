# Young Physicist
a = int(input())
inputs = [input() for i in range(a)]

sum_x = 0
sum_y = 0
sum_z = 0
for i in inputs:
    j = i.split()
    sum_x += int(j[0])
    sum_y += int(j[1])
    sum_z += int(j[2])

if sum_x == 0 and sum_y == 0 and sum_z == 0:
    print('YES')
else:
    print('NO')
