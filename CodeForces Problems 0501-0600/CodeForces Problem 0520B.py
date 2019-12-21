from math import *


nums = input().split()
n = int(nums[0])
m = int(nums[1])


def mincount(n, m):
    count = 0
    if n > m:
        count = n - m
    elif n < m:
        if m % 2 == 0:
            count = mincount(n, m // 2) + 1
        if m % 2 == 1:
            count = mincount(n, m + 1) + 1
    return count


print(mincount(n,m))
