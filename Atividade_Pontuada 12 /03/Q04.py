import os

os.system("clear")


morango_kg = float(input("Digite a quantidade de morangos em KG: "))
maca_kg = float(input("Digite a quantidade de maçãs em KG: "))


if morango_kg <= 5:
    preco_morango = morango_kg * 2.50
else:
    preco_morango = morango_kg * 2.20   


if maca_kg <= 5:
    preco_maca = maca_kg * 1.50
else:
    preco_maca = maca_kg * 1.80  


total = preco_morango + preco_maca


if morango_kg + maca_kg >= 10:
    total *= 0.90  
else:
    if total > 15.00:
        total *= 0.90  


print(f"O valor total a ser pago pelo cliente é: R$ {total:.2f}")