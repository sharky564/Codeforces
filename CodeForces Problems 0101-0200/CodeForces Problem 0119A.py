# Epic Game

from math import gcd
a=input()
b=a.split()
pile=int(b[2])
i=1
while pile>0:
    if i%2==1:
        pile=pile-gcd(pile,int(b[0]))
    else:
        pile=pile-gcd(pile,int(b[1]))
    i+=1

if i%2==1:
    print('1')
else:
    print('0')
