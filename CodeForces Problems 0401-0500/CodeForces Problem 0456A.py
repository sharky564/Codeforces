# Laptops
n = int(input())
qual = [input() for i in range(n)]
quality = []
for i in qual:
    k = i.split()
    quality.append([int(k[1]), int(k[0])])

quality.sort()
i = 0
while i < n - 1:
    if quality[i][1] < quality[i + 1][1]:
        i += 1
    else:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
