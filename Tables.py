n,r=map(int,input().split())
for i in range(1,r+1):
    if(i%2==1):
        print(f"{n} x {i} = {n*i}")