# Beautiful Year
a=int(input())

def f(n):
    b=list(str(n+1))
    digits=[]
    for i in b:
        digits.append(i)
    digits=set(digits)
    if len(digits)==len(b):
        return n+1
    else:
        return f(n+1)

print(f(a))
