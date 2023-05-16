t=int(input())
for i in range(1,t+1):
    n,a,b,k=map(int,input().split())
    inter=n/(a*b)
    u=n/a+n/b-inter
    if(u>=k):
        print("Win")
    else:
        print("Lose")