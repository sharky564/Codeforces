# Anton and Digits
k = input().split()
k2 = int(k[0])
k3 = int(k[1])
k5 = int(k[2])
k6 = int(k[3])
k256 = min(k2, k5, k6)
k32 = min(k3, k2 - k256)
print(k256 * 256 + k32 * 32)
