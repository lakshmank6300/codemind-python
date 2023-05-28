n=int(input())
mx=0
ls=list(map(int,input().split()))
for i in ls:
    if(ls.count(i)==1):
        if(i>mx):
            mx=i
if(mx==0):
    print(-1)
else:
    print(mx)