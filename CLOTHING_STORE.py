n=int(input())
ls=list(map(int,input().split()))
ls.sort()
i=0
c=0
while(i<n-1):
    if(ls[i]==ls[i+1]):
        i+=2
        c+=1
    else:
        i+=1
print(c)
    
    