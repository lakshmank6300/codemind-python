def self_divide(n):
    for i in n:
        if(int(i)==0):
            return False
        if(int(n)%int(i)!=0):
            return False
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(self_divide(str(i))):
        print(i,end=' ')