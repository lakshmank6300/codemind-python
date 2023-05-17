n=int(input())
if(n<3):
    print("The pattern is not possible")
else:
    for i in range(1,n+1):
        k=1
        for j in range(i,n+1):
            print("%d"%(k),end='')
            k+=1
        print("")

        