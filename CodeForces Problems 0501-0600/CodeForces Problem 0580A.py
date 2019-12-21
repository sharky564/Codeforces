a=int(input())
b=input()
c=b.split()
locmax=1
globmax=1
i=0
while i<a-1:
  if int(c[i])<=int(c[i+1]):
    if i!=a-2:
      if int(c[i+1])<=int(c[i+2]):
        locmax+=1
      else:
        locmax+=1
        if locmax>globmax:
          globmax=locmax
        locmax=1
    else:
      locmax+=1
      if locmax>globmax:
        globmax=locmax
        locmax=1
  i+=1
print(globmax)
