import numpy

print("////PRIMOS E SUAS POSIÇÕES////")

TAMANHO = 2

vetor = numpy.zeros(TAMANHO, dtype=int)

#Preenche o vetor
for i in range(TAMANHO):
    vetor[i] = int(input("Número inteiro: "))

print()

#Passa pelo vetor fazendo a verificação de primos
for i in range(TAMANHO):
    qtdDivExatas = 0
    num = vetor[i]
    for j in range(1, num+1):
        if num % j == 0:
            qtdDivExatas+=1
    if qtdDivExatas == 2:
        print(f'{num} é primo e está no índice {i}')
    else:
        print(f'{num} NÃO é primo e está no índice {i}')
        