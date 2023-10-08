n=int(input())
p=[]
for i in range(n):
    ls=list(map(str,input().split()))
    p.append(ls)
print(p[-1][-1])
    