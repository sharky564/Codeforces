# Minimum Ternary String
s = input()
n = int(s)
m = len(s)
k = list(s)
index0 = [i for i, x in enumerate(k) if x == '0']
index1 = [i for i, x in enumerate(k) if x == '1']
index2 = [i for i, x in enumerate(k) if x == '2']

output = ''
while len(index2) != 0 and len(index0) != 0:
    if max(index0) > max(index2):
        output = '0' + output
        index0.remove(max(index0))
    else:
        output = '2' + output
        index2.remove(max(index2))

output = len(index0) * '0' + len(index1) * '1' + len(index2) * '2' + output
print(output)
