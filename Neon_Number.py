n=int(input())
s=0
k=str(n*n)
for i in k:
    s=s+int(i)
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")
    