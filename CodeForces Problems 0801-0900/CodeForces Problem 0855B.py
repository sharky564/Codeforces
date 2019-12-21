a=input().split()
array0=input().split()
array=[int(i) for i in array0]
array1=[i for i in array]
n=int(a[0])
p=int(a[1])
q=int(a[2])
r=int(a[3])
arrayr=[r*i for i in array]
k=max((x, i) for i, x in enumerate(arrayr))[1]+1
arrayq=[q*i for i in array[:k]]
l=max((x, i) for i, x in enumerate(arrayq))[1]+1
arrayp=[p*i for i in array[:l]]
print(max(arrayr)+max(arrayq)+max(arrayp))
