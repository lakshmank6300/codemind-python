n=int(input())
ls=list(map(int,input().split()))
ls.sort()
c=0
for i in ls:
    if(ls.count(i)==1):
        print(i,end=" ")
        c=1
if(c==0):
    print("-1")