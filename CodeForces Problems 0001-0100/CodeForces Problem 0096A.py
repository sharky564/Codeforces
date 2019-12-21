# Football
a = input()
b = []
for k in a:
    b.append(int(k))

if len(b) < 7:
    print('NO')
elif len(b) >= 7:
    i = 0
    while i <= len(b) - 7:
        if sum(b[i:i + 7]) % 7 == 0:
            print("YES")
            break
        else:
            i += 1
    else:
        print("NO")
