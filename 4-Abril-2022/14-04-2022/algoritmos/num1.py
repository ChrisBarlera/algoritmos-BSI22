# Faça um programa que receba o salário base de um funcionário, calcule e mostre
# o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o
# salário base e paga 7% de imposto também sobre o salário base

salario = float(input("Insira o salário base: "))
liquido = (salario * 1.05) - (salario * 0.07)
print("Salário líquido é:",liquido) 