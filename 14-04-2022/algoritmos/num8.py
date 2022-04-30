# Um restaurante a quilo cobra R$45,00 o Kg de refeição. Escreva um algoritmo
# que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a
# pagar. Lembre-se que deve ser informado o peso do prato (tara), para que seja
# descontado do peso total.

peso_montado = float(input("Peso do prato MONTADO em Kg: "))
prato = float(input("Peso do prato (tara) em Kg: "))
total = (peso_montado - prato) * 45
print("Valor total: R$",total)