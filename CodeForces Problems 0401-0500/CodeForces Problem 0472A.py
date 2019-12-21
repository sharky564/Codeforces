a=int(input())
list1=[]
if a%2==0:
    list1.append(str(4))
    list1.append(str(a-4))
else:
    list1.append(str(9))
    list1.append(str(a-9))

print(" ".join(list1))
