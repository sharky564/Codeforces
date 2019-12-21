# Dubstep
import re
a=input()
b=list(a)
i=0
if len(b)<3:
  print(a)
else:
  while b[0]+b[1]+b[2]=='WUB':
    b=b[3:]
    if len(b)<3:
      print(''.join(b))
      break
  else:
    c=''.join(b)
    d=list(c[::-1])
    if len(d)<3:
      print(c[::-1])
    else:
      while d[0]+d[1]+d[2]=='BUW':
        d=d[3:]
        if len(d)<3:
          print(''.join(d)[::-1])
          break
      else:
        e=''.join(d)[::-1]
        result1 = re.sub('WUB',' ', e)
        result = re.sub('\ \ +',' ', result1)
        print(result)
