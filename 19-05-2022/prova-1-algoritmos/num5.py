# Aluno: Christian Honorato Barlera de Andrade
# Turma: BSI22

# Aumento de salário;
# Salários > 1100 aumenta 10% enquanto menores aumenta 15%.

salario = float(input("Salário do funcionário: "))

if salario > 1100:
    salario = salario*1.1
else:
    salario = salario*1.15

print("O salário após o aumento é:",salario)