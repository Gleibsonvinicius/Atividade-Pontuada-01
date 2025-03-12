
import os

os.system("clear")


renda_mensal = float(input("Digite a sua renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado: R$ "))
numero_prestacoes = int(input("Digite o número de prestações desejadas: "))


prestacao = valor_emprestimo / numero_prestacoes


limite_emprestimo = 10 * renda_mensal
limite_prestacao = 0.30 * renda_mensal


if valor_emprestimo > limite_emprestimo:
    print("Empréstimo não pode ser concedido: valor do empréstimo excede o limite permitido.")
    
elif prestacao > limite_prestacao:
    print("Empréstimo não pode ser concedido: valor da prestação excede 30% da renda mensal.")
    
else:
    print("Empréstimo pode ser concedido.")