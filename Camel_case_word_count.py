s=input()
cnt=0
for i in s:
    if i>='A' and i<='Z':
        cnt+=1;
if(s[0]>='a' and s[0]<='z'):
    cnt+=1;
print(cnt)