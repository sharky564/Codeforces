nums = input().split()

num = int(nums[0])
count = int(nums[1])

def sub(n):
    if n % 10 != 0:
        return n - 1
    else:
        return n // 10

k = 0
result = num
while k < count:
    result = sub(result)
    k += 1

print(result)
