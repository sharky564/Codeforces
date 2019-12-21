from math import ceil
a=input()
b=a.split()
cost=0
if int(b[1])/int(b[3])>1/int(b[2]):
    if int(b[3])<(int(b[0])%int(b[1]))*(int(b[2])):
    	cost+=ceil((int(b[0])/int(b[1])))*int(b[3])
    else:
    	cost+=(int(b[0])//int(b[1]))*int(b[3])+(int(b[0])%int(b[1]))*(int(b[2]))
else:
    cost+=int(b[0])*int(b[2])

print(cost)
