a=int(input())
b=[]
for i in range(a):
    k=input()
    if k not in b:
        b.append(k)
        print("NO")
    else:
        print("YES")
