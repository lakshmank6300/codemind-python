m,n=map(int,input().split())
if(m==1 and n==1):
    print("Player 2")
else:
    if(m%2==0 or n%2==0):
        print("Player 1")
    else:
        print("Player 2")