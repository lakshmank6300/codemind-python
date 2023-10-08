s=input()
mx=1
ans=1
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        mx+=1
    else:
        mx=1
    ans=max(ans,mx)
print(ans)
    
    