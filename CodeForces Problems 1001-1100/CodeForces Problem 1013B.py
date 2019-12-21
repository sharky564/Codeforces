# And
temp = input().split()
n = int(temp[0])
x = int(temp[1])
a = [int(i) for i in input().split()]

if len(set(a)) != len(a):
    print('0')
else:
    b = []
    for i in a:
        if i > x:
            j = i & x
            if j in a:
                print('1')
                break
            else:
                b.append(j)
    else:
        if len(set(b)) != len(b):
            print('2')
        else:
            print('-1')
