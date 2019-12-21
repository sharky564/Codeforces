s = input()
while "AB" in s and "BA" in s:
    x,y = s.split("AB",1)
    if "BA" in x or "BA" in y:
        print("YES")
        break
    else:
        s = s.replace("AB","",1)
else:
    print("NO")
