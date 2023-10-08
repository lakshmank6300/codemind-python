s=input()
cnt=0
mx=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        cnt+=1
    else:
        cnt=0
    mx=max(mx,cnt)
print(mx)