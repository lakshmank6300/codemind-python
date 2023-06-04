n=input()
s=0
for i in range(0,len(n)):
    s=int(n[i])**int(i+1)+s
if(s==int(n)):
    print(True)
else:
    print(False)
    
    