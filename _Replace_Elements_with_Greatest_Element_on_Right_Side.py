n=int(input())
ls=list(map(int,input().split()))
for i in range(0,n-1):
    m=0
    for j in range(i+1,n):
        if(ls[j]>m):
            m=ls[j]
    ls[i]=m
ls[n-1]=-1
for i in ls:
    print(i,end=" ")