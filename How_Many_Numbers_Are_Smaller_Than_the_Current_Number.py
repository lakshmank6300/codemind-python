n=int(input())
ls=list(map(int,input().split()))
lst=[i for i in ls]
ls.sort()
for i in range(0,len(lst)):
    print(ls.index(lst[i]),end=" ")
        