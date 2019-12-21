a = int(input())
b=input()
c=b.split()
s = [0] * 100002
for i in map(int, c):
    s[i] += i
x = y = 0
for i in s:
    x, y = max(x, y), x+i
print(x)
