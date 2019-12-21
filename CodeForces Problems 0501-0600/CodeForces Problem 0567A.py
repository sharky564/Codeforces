# Lineland Mail
n = int(input())
x = [int(i) for i in input().split()]

i = 0
while i < n:
    if i == 0:
        mini = x[1] - x[0]
        maxi = x[-1] - x[0]
    elif i == n-1:
        mini = x[-1] - x[-2]
        maxi = x[-1] - x[0]
    else:
        mini = min(x[i] - x[i - 1], x[i + 1] - x[i])
        maxi = max(x[-1] - x[i], x[i] - x[0])
    print(mini, maxi)
    i += 1
