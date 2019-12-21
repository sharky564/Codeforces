calories = [int(i) for i in input().split()]
strips = list(input())
wasted = 0
for i in strips:
    wasted += calories[int(i) - 1]

print(wasted)
