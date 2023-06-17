import math
n=int(input())
lst=list(map(int,input().split()))
k=lst[0]
for i in range(1,len(lst)):
    k=math.lcm(k,lst[i])
print(k)