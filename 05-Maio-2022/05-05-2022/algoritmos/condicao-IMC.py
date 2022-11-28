altura = float(input("Altura do adulto (em metros): "))
peso = float(input("Peso do adulto (em Kg): "))

valor_imc = peso / altura**2

if valor_imc < 18.5:
    print("Abaixo do peso")
if valor_imc >= 18.5 and valor_imc < 25:
    print("Peso normal")
if valor_imc >=25 and valor_imc <=30:
    print("Acima do peso")
if valor_imc > 30:
    print("Obeso")