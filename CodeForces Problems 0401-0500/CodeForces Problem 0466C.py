n = int(input())
a = list(map(int, input().split()))
parsum = [0] * n
for i in range(n):
    if i == 0:
        parsum[i] = a[0]
    else:
        parsum[i] = parsum[i - 1] + a[i]

thirds = list(filter(lambda x: x == parsum[-1] / 3 or x == 2 * parsum[-1] / 3, parsum[:n - 1]))

if len(set(thirds)) == 0:
    print(0)
else:
    output = 0
    i = 0
    while i < len(thirds):
        if thirds[i] == parsum[-1] / 3:
            output += thirds[i + 1:].count(2 * parsum[-1] / 3)
        i += 1
    print(output)
