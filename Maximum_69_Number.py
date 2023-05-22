n=input()
lst=[]
lst=[int(i) for i in n]
for i in range(0,len(lst)):
    if(lst[i]==6):
        lst[i]=9
        break
for i in lst:
    print(i,end='')