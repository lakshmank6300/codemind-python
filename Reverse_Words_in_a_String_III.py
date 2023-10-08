s=input()
st=""
for i in s:
    if i==" ":
        print(st[::-1],end=" ")
        st=""
    else:
        st+=i
print(st[::-1])
    
    