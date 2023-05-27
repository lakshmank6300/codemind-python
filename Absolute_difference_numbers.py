import math
n,dig=map(int,input().split())
d=int(math.log10(n)+1)
sl=10**dig
sf=10**(d-dig)
f=int(n/sf)
l=int(n%sl)
print(abs(f-l))
