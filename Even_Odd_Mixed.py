n=(input())
e=0
o=0
for i in n:
    i=int(i)
    if(i%2==0):
        e+=1
    else:
        o+=1
if(e!=0 and o==0):
    print("Even")
elif(e==0 and o!=0):
    print("Odd")
else:
    print("Mixed")
