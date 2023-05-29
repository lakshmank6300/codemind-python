n=int(input())
ls=list(map(int,input().split()))
c=0
for i in ls:
    if i!=0:
        print(i,end=" ")
    else:
        c+=1
for i in range(0,c):
    print(0,end=" ")