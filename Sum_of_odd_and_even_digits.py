n=int(input())
ls=list(map(int,input().split()))
os=0
es=0
for i in range(0,n):
    if(i%2==0):
        os+=ls[i]
    else:
        es+=ls[i]
if(os-es==0):
    print("YES")
else:
    print("NO")