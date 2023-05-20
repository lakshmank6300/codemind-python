n=int(input())
s=0
p=1
while(n>0):
    r=n%10
    #print(r)
    s=s+r
    p=p*r
    n=n//10
#print(s)
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")