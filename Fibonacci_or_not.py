n=int(input())
a=0
b=1
k=0
for i in range(1,n):
    c=a+b
    a=b
    b=c
    if(a==n):
        print(True)
        k=1
        break
if k==0:
    print(False)