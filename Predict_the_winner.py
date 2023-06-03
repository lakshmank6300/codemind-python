n=int(input())
ls=list(map(int,input().split()))
sx=0
for i in range(0,int(n/2)):
    sx+=ls[i]
sy=sum(ls)-sx
if(abs(sy-sx)%4==0):
    print("X")
else:
    print("Y")
    
        