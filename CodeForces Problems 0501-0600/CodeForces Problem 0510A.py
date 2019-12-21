a=input()
b=a.split()
table = []
for x in range(int(b[0])):
    if x%2==0:
        table.append(['#']*int(b[1]))
    else:
        if x%4==1:
            table.extend([['.'*(int(b[1])-1),'#']])
        else:
            table.extend([['#','.'*(int(b[1])-1)]])

for row in table:
    print(''.join(row))
