contador = 1
soma = 0
limiteIntervalo = 10

while contador <= limiteIntervalo:
    print(contador)
    soma = soma + contador
    contador = contador + 1
print("\nA média de todos os números é: ",soma/limiteIntervalo)