# Pashmak and Flower
n = int(input())
b = [int(i) for i in input().split()]
bmax = max(b)
bmin = min(b)
maxocc = b.count(bmax)
minocc = b.count(bmin)
maxbeau = bmax - bmin
if bmax != bmin:
    beauocc = maxocc * minocc
else:
    beauocc = (maxocc**2 - maxocc)//2
print(maxbeau, beauocc)
