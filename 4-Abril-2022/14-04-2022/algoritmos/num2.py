# Faça um programa que receba o valor de um depósito e o valor da taxa de juros
# anual, calcule e mostre o valor do rendimento e o valor total depois do
# rendimento (após 1 ano);

deposito = float(input("Valor do depósito: "))
juros = float(input("Taxa de juros anual: "))
valor_total = deposito * (1 + juros / 100)
print("O valor total após o rendimento de um ano é:",valor_total)