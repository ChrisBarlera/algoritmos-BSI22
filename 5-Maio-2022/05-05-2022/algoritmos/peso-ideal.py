altura = float(input("Altura da pessoa: "))
sexo = input("Sexo da pessoa (M ou F): ")

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
if sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7

print("O peso ideal é:",peso_ideal)