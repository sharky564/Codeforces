# Is your horseshoe on the other hoof?
a=input()
b=a.split()
b=set(b)
if len(b)<=3:
    print(4-len(b))
else:
    print(0)
