linha = input().split(" ")
A, B, C = linha

A = int(A)
B = int(B)
C = int(C)

D = ((A+B+abs(A-B))/2)
maior = ((C+D+abs(C-D))/2)

print("{} eh o maior".format(int(maior)))