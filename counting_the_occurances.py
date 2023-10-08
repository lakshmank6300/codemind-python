s=input()
t=input()
cnt=0
for i in s:
    if i==t:
        cnt+=1
if cnt==0:
    print(-1)
else:
    print(cnt)