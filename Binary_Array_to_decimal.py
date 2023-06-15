n=int(input())
ls=list(map(int,input().split()))
c=0
s=0
for i in range(-1,-n-1,-1):
    s+=ls[i]*(2**c)
    c+=1
print(s)