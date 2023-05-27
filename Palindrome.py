def pal(n):
    if(n==n[::-1]):
        return True
    else:
        return False
n=int(input())
print(pal(str(n)))

 
 