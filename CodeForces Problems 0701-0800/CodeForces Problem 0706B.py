n = int(input())
prices = list(map(int, input().split()))
days = int(input())
coins = [int(input()) for i in range(days)]

def solve(money, costs):
    lower = 0
    upper = len(costs) - 1
    while upper > lower + 1:
        middle = (upper + lower) // 2
        if costs[middle] <= money:
            lower = middle
        elif costs[middle] >= money:
            upper = middle
    if costs[upper] <= money:
        return upper + 1
    elif costs[lower] <= money:
        return upper
    elif costs[lower] > money:
        return lower

prices = sorted(prices)
for coin in coins:
    print(solve(coin, prices))
