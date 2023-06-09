def pal(n:str)->int:
    k=n
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n//=10
    return k==s
def prev_pal(n):
    while(n):
        if(pal(n)):
            break
        else:
            n-=1
    return n
def next_pal(n):
    while(n):
        if(pal(n)):
            break
        else:
            n+=1
    return n
n=int(input())
fn=prev_pal(n-1)
bn=next_pal(n+1)
if(n-fn==bn-n):
    print(fn,bn)
elif(n-fn<bn-n):
    print(fn)
else:
    print(bn)