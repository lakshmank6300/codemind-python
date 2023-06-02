def is_vowel(i):
    if(i=='a' or i=='e' or i=='o' or i=='i' or i=='u'):
        return 1
    else:
        return 0
n=input()
if(is_vowel(n[0])):
    print('V',end='')
else:
    print('C',end='')
for i in range(1,len(n)):
    if is_vowel(n[i]):
        if(is_vowel(n[i-1])==0):
            print('V',end='')
    else:
        if(is_vowel(n[i-1])):
            print('C',end='')