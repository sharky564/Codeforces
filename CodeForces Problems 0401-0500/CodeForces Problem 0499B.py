numwords = input().split()
n = int(numwords[0])
m = int(numwords[1])
words = [input().split() for i in range(m)]
lan1 = [i[0] for i in words]
lan2 = [i[1] for i in words]
translate = input().split()

new = translate
k = 0
while k < m:
    if len(lan1[k]) > len(lan2[k]):
        new = list(map(lambda x: lan2[k] if x == lan1[k] else x, new))
    k += 1

exp = ' '.join(i for i in new)
print(exp)
