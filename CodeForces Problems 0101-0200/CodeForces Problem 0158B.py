# Taxi
from math import ceil


a = input()
b = input()
c = b.split()
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in c:
    if i == '1':
        count1 += 1
    if i == '2':
        count2 += 1
    if i == '3':
        count3 += 1
    if i == '4':
        count4 += 1

count = 0
w = count4
y = count2//2
if count1 <= count3:
    count += count3 + (count2 % 2)
elif count1 > count3:
    if count2 % 2 == 1:
        if count1 - count3 <= 2:
            count += 1 + count3
        elif count1 - count3 > 2:
            count += ceil((count1 - count3 - 2) / 4) + 1 + count3
    elif count % 2 == 0:
        count += ceil((count1 - count3) / 4) + count3

print(count + w + y)
