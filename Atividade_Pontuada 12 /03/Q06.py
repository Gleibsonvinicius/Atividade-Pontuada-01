import os

os.system("clear")




nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2


print(f"A média do aluno é: {media:.2f}")


if media >= 6.0:
    print("Parabéns! O aluno está aprovado.")
elif media >= 4.0:
    print("O aluno está em recuperação.")
else:
    print("O aluno foi reprovado.")