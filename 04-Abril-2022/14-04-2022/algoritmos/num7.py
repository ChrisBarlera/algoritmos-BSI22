# Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um
# algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir
# quantos litros ele conseguiu colocar no tanque.

reais_pagos = float(input("Valor total pago em reais: "))
valor_litro = float(input("Valor do litro: "))
litros = reais_pagos / valor_litro
print("Litros colocados:",litros)