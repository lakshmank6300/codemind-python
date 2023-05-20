def fact(n):
    p=1
    for i in range(1,int(n)+1):
        p=p*i
    return p
n=input()
s=0
for i in n:
    s=s+fact(i)
if(s==int(n)):
    print("The number %d is a strong number"%(int(n)))
else:
    print("The number %d is not a strong number"%(int(n)))
