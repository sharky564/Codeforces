numbers = [int(i) for i in input().split()]
big = max(numbers)
output = []
for number in numbers:
    if number != big:
        output.append(str(big - number))

print(' '.join(output))
