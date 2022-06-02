inicioIntervalo = int(input("Início do intervalo: "))
fimIntervalo = int(input("Fim do intervalo: "))
soma = 0

while inicioIntervalo <= fimIntervalo:
    if inicioIntervalo % 2 == 0:
        soma = soma + inicioIntervalo
        print(inicioIntervalo)
    inicioIntervalo += 1
print("A soma de todos os pares é:",soma)