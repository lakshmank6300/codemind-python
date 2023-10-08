s=input()
U=s.count('U')
D=s.count("D")
R=s.count("R")
L=s.count("L")
if(U==D and R==L):
    print("True")
else:
    print("False")