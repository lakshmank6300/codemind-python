n=int(input())
ls=list(map(int,input().split()))
mx=0
c=0
mn=max(ls)
for i in ls:
    if(ls.count(i)==i):
        mx=max(i,mx)
        mn=min(i,mn)
        c=1
if(c==0):
    print(-1)
else:
    print(mn,mx)