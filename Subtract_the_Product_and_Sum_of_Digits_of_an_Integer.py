n=(input())
s=0
p=1
for i in n:
    s=s+int(i)
    p=p*int(i)
print(p-s)