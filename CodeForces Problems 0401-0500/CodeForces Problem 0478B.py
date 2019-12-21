# Random Teams
teams = input().split()
n = int(teams[0])
m = int(teams[1])

def friends(n):
    return (n ** 2 - n) // 2

mint = n // m
rem = n % m
minf = friends(mint) * (m - rem) + friends(mint + 1) * rem

maxt = n - m + 1
maxf = friends(n - m + 1)

print(minf, maxf)
