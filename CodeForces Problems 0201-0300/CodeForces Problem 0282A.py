# Bit++
a = int(input())
inputs = [input() for i in range(a)]


def f(x, input):
    for i in input:
        if i in ['--X', 'X--', '-X-']:
            x -= 1
        elif i in ['++X', 'X++', '+X+']:
            x += 1
    return x

print(f(0, inputs))
