x = list(input())

i = 0
while i < len(x):
    if i == 0:
        if 4 < int(x[i]) < 9:
            x[i] = str(9 - int(x[i]))
    elif int(x[i]) > 4:
        x[i] = str(9 - int(x[i]))
    i += 1

exp = ''.join(x)
print(exp)
