import os

os.system("clear")



A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))


if A == B:
    C = A + B  
else:
    C = A * B 


print("O resultado é:", C)