def prime(n):
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return False
    return True
def next_prime(n):
    while(n):
        if(prime(n)):
            return n
        n+=1
def prev_prime(n):
    while(n):
        if(prime(n)):
            return n
        n-=1
t=int(input())
for i in range(0,t):
    n=int(input())
    if(next_prime(n)-n<n-prev_prime(n)):
        print(next_prime(n))
    else:
        print(prev_prime(n))
