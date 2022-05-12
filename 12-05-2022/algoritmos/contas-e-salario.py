salario = float(input("Salário: "))
conta1 = float(input("Conta 1: "))
conta2 = float(input("Conta 2: "))
print("\n////////////////////////////////////////\n")

conta1 = conta1 * 1.02
conta2 = conta2 * 1.02
salario = salario - (conta1 + conta2)

print("Resto do salário:",salario)