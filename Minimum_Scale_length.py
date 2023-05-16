import math
n=int(input())
lst=list(map(int,input().split()))
k=lst[0]
for i in range(2,n):
    k=math.gcd(lst[i],k)
print(k)