t=int(input())
while(t):
    st=input()
    res=st[::-1]
    if(st==res):
        print("YES ",end="")
        if(len(st)%2==1):
            print("ODD")
        else:
            print("EVEN")
    else:
        print("NO")
    t-=1
        