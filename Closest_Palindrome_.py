def pal(n):
    if(n==n[::-1]):
        return True
    else:
        return False
def prev_pal(n):
    while(n):
        if(pal(str(n))):
            return n
        n-=1
def next_pal(n):
    while(n):
        if(pal(str(n))):
            return n
        n+=1
n=int(input())
f=prev_pal(n-1)
l=next_pal(n+1)
if(n-f==l-n):
    print(f,l)
elif(n-f<l-f):
    print(f)
else:
    print(l)
 
 