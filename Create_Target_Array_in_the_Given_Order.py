n=int(input())
ins=list(map(int,input().split()))
ni=int(input())
ind=list(map(int,input().split()))
tar=[]
for i in range(0,n):
    tar.insert(ind[i],ins[i])
for i in tar:
    print(i,end=" ")