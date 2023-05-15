def prime(n):
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if(i!=1):
        if(prime(i)==1):
           c+=1
print(c)