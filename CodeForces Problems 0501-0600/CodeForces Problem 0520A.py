a=int(input())
b=input()
c=list(b.lower())
if a<26:
    print('NO')
else:
    letters = []
    for i in c:
        if i not in letters:
            letters.append(i)
    if len(letters)==26:
        print('YES')
    else:
        print('NO')
