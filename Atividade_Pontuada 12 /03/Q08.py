import os

os.system("clear")


cor_cd = input("Digite a cor do CD (VERDE, AZUL, AMARELO, VERMELHO): ").strip().upper()


if cor_cd == "VERDE":
    preco = 10.00
elif cor_cd == "AZUL":
    preco = 20.00
elif cor_cd == "AMARELO":
    preco = 30.00
elif cor_cd == "VERMELHO":
    preco = 40.00
else:
    print("Cor inválida! Por favor, insira uma cor válida.")


if preco > 0:
    print(f"O preço do CD {cor_cd} é R$ {preco:.2f}")