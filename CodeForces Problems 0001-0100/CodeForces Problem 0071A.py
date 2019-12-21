# Way Too Long Words
a = int(input())
inputs = [input() for i in range(a)]

for i in inputs:
    if len(i) <= 10:
        print(i)
    elif len(i) > 10:
        b = list(i)
        c = len(b)-2
        print(b[0] + str(c) + b[len(b) - 1])
