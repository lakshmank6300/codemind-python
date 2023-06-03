n=int(input())
ls=list(map(int,input().split()))
lst=[]
i=0
while(i<n-1):
    for j in range(0,ls[i]):
        lst.append(ls[i+1])
    i+=2
for i in lst:
    print(i,end=" ")