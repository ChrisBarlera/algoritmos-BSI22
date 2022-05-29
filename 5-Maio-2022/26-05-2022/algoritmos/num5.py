litros = float(input("Litros vendidos: "))
tipo = input("Tipo de combustível(A ou G): ")

precoAlcool = 6.5
precoGasolina = 7.2
if tipo == "A":
    valorInicial = precoAlcool * litros
    if litros < 20:
        desconto = valorInicial * 0.03
        valorFinal = valorInicial - desconto
        print(valorFinal)
else :
    valorInicial = precoGasolina * litros
    
