n=input()
ls=[i for i in n]
for i in range(0,len(ls)):
    if(ls[i]=='6'):
        ls[i]='9'
        break
for i in ls:
    print(i,end='')
    