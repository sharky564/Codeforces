sizes = [int(i) for i in input().split()]
n = sizes[0]
m = sizes[1]
array = [int(i) for i in input().split()]
line = [int(input()) for i in range(m)]

for i in line:
    print(len(set(array[i-1:])))
