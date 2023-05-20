n=int(input())
a=0
b=1
while(1):
    c=a+b
    a=b
    b=c
    if(c<n):
        m=c
    else:
        mx=c
        break

if(n-m<mx-n):
    print(m)
elif n-m==mx-n:
    print(m,mx)
else:
    print(mx)
    