def rev(n:int) ->int:
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n//=10
    return s
n=int(input())
nr=rev(n)
if(n**2==rev(nr**2)):
    print("True")
else:
    print("False")