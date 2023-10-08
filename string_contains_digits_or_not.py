t=int(input())
while(t):
    flag="No"
    st=input()
    for i in st:
        if i>="0" and i<="9":
            flag="Yes"
            break
    print(flag)
    t-=1
            