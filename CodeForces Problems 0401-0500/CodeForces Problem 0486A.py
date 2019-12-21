a=int(input())
def f(n):
    if n%2==0:
        return n/2
    elif n%2==1:
        return -(n+1)/2

print(int(f(a)))
