n=int(input())
c=1
lst=list(map(int,input().split()))
for i in lst:
    if i>=n:
        c=0
        break
if(c==1):
    print("YES")
else:
    print("NO")