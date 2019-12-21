# Team
a = int(input())
inputs = [input() for i in range(a)]

count = 0
for i in inputs:
    total = 0
    j = str(i).split()
    for k in j:
        total += int(k)
    if total >= 2:
        count += 1

print(count)
