text = input()
n = len(text)
m = int(input())
queries = [list(int(i) - 1 for i in input().split()) for j in range(m)]

same = [0] * n
for i in range(1, n):
    if text[i] == text[i - 1]:
        same[i] = same[i - 1] + 1
    else:
        same[i] = same[i - 1]

for query in queries:
    print(same[query[1]] - same[query[0]])
