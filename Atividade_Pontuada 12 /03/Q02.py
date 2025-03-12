import os

os.system("clear")



# Leitura dos dados do usuário
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ")
estado_civil = input("Digite seu estado civil: ")


tempo_casada = None


if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite o tempo de casada (em anos): "))


print("\nDados do Usuário:")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")


if tempo_casada :
    print(f"Tempo de Casada: {tempo_casada} anos")
