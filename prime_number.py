def prime(n):
    if(n==1):
        return False
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return False
    return True
n=int(input())
if(prime(n)):
    print("prime")
else:
    print("not a prime")