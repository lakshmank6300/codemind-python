n=int(input())
ls=list(map(int,input().split()))
e=[]
o=[]
for i in ls:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
print(*o,end=" ")
print(*e)