s=input()
cnt=0;
for i in s:
    if(i>="0" and i<="9"):
        cnt+=1
if(cnt==0):
    print("Doesn't contain digit")
else:
    print(f"Contains {cnt} digit")