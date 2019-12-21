# The number of positions

num = [int(i) for i in input().split()]
n = num[0]
a = num[1]
b = num[2]

print(n - max(a + 1, n - b) + 1)
