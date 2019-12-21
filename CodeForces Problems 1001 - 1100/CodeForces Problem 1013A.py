# Piles With Stones
n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

if sum(x) >= sum(y):
    print('Yes')
else:
    print('No')
