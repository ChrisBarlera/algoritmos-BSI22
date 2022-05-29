litros = float(input("Litros vendidos: "))
tipo = input("Tipo de combustível(A ou G): ")

precoAlcool = 6.5
precoGasolina = 7.2
if tipo == "A":
    if litros <= 20:
        # desconto de 3% por litro
        resultado = (precoAlcool * 0.97) * litros
        print("Valor a ser pago (com desconto):",resultado)
    else:
        # desconto de 5% por litro
        resultado = (precoAlcool * 0.95) * litros
        print("Valor a ser pago (com desconto):",resultado)
else:
    if litros <= 20:
        # desconto de 4% por litro
        resultado = (precoGasolina * 0.96) * litros
        print("Valor a ser pago (com desconto):",resultado)
    else:
        # desconto de 6% por litro
        resultado = (precoGasolina * 0.94) * litros
        print("Valor a ser pago (com desconto):",resultado)