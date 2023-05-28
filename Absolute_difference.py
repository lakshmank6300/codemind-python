def prime(n):
    k=int(n**0.5)
    for i in range(2,k+1):
        if(n%i==0):
            return False
    return True
n=int(input())
ls=list(map(int,input().split()))
p=1
np=1
for i in ls:
    if(prime(i)):
        p*=i
    else:
        np*=i
print(abs(p-np))