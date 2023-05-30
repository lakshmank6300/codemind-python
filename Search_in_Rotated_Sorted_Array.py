n=int(input())
ls=list(map(int,input().split()))
k=int(input())
c=0
for i in range(0,n):
    if(ls[i]==k):
        c=1
        print(i)
        break
if(c==0):
    print(-1)