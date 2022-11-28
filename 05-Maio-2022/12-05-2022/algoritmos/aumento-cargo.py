codigo = int(input("Código do cargo: "))
salario = float(input("Salário atual: "))
print("\n///////////////////////////\n")

if codigo == 1:
    cargo = "Escrituário"
    salario = salario * 1.5
elif codigo == 2:
    cargo = "Secretário"
    salario = salario * 1.35
elif codigo == 3:
    cargo = "Caixa"
    salario = salario * 1.20
elif codigo == 4:
    cargo = "Gerente"
    salario = salario * 1.1
else:
    cargo = "Diretor"

print(cargo,":",salario,"(novo salário)")