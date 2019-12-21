# Queue at the School
a=input()
b=input()
c=a.split()
def f(m,n):
    if n==0:
        return m
    else:
        m=m.replace('BG','GB')
        return f(m,n-1)

print(f(b,int(c[1])))
