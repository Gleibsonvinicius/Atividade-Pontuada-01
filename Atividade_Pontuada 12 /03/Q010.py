import os

os.system("clear")





preco_alcool = 3.79
preco_gasolina = 6.59


litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").strip().upper()




if tipo_combustivel == 'A':
    if litros_vendidos <= 25:
        desconto = 0.02  
    else:
        desconto = 0.04  
    valor_a_pagar = litros_vendidos * preco_alcool * (1 - desconto)

elif tipo_combustivel == 'G':
    if litros_vendidos <= 25:
        desconto = 0.03  
    else:
        desconto = 0.05  
    valor_a_pagar = litros_vendidos * preco_gasolina * (1 - desconto)

else:
    print("Tipo de combustível inválido! Por favor, insira 'A' para Álcool ou 'G' para Gasolina.")


if tipo_combustivel in ['A', 'G']:
    print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")