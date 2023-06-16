def prime(n):
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return False
    return True
a=int(input())
b=int(input())
for i in range(a+1,b):
    if(prime(i)):
        print(i)