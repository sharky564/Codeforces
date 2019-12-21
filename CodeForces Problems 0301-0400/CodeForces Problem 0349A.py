# Cinema Line

n = int(input())
bill = [int(j) for j in input().split()]

change = [0,0]
k = 0
while k < n:
    if bill[k] == 25:
        change[0] += 1
        k += 1
    elif bill[k] == 50:
        if change[0] == 0:
            print("NO")
            break
        else:
            change[0] -= 1
            change[1] += 1
            k += 1
    elif bill[k] == 100:
        if change[0] >= 1 and change[1] >= 1:
            change[0] -= 1
            change[1] -= 1
            k += 1
        elif change[0] >= 3:
            change[0] -= 3
            k += 1
        else:
            print("NO")
            break
else:
    print("YES")
