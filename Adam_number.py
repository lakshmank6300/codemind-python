n=(input())
n1=n[::-1]
sn=int(n)**2
sn1=str(int(n1)**2)
revsn1=sn1[::-1]
if(str(sn)==str(revsn1)):
    print(True)
else:
    print(False)