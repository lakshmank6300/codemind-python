def prime(n):
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return False
    return True
n=int(input())
c=0
for i in range(0,n):
    if prime(i):
        for j in range(0,n):
            if(prime(j)):
                if i*j==n:
                    print(i,j)
                    c=1
                    break
        if(c==1):
            break
if(c==0):
    print(-1)