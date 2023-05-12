n=int(input())
for i in range(1,n+1):
    k=1
    for j in range(i,n+1):
        print("%d "%(j),end="")
        k+=1
    print()