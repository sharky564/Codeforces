a=input()
b=a.split()
total=int(b[0])*(int(b[2])**2+int(b[2]))/2
if int(b[1])>=total:
    print('0')
else:
    print(int(total-int(b[1])))
