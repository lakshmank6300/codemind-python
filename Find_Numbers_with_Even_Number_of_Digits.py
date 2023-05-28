import math
n=int(input())
ls=list(map(int,input().split()))
c=0
#print(math.log10(1000)+1)
for i in ls:
    if(int((math.log10(i))+1)%2==0):
        c+=1
print(c)