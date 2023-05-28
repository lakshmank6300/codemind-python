n=int(input())
ls=list(map(int,input().split()))
m=max(ls)
k=int(input())
lst=[]
for i in range(0,n):
    if(ls[i]+k>=m):
        lst.append(True)
    else:
        lst.append(False)
for i in lst:
    print(i,end=" ")