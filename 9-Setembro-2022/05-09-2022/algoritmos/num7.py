import numpy

print('////DIFERENÇA DE VETORES////')

TAMANHO = 10

primeiroArray = numpy.zeros(TAMANHO, dtype=int)
segundoArray = numpy.zeros(TAMANHO, dtype=int)

print('\nPrimeiro vetor:')
for i in range(TAMANHO):
    primeiroArray[i] = int(input('Número inteiro: '))

print('\nSegundo vetor:')
for i in range(TAMANHO):
    segundoArray[i] = int(input('Número inteiro: '))

#Montando a lista de diferença
diferenca = []
for i in range(TAMANHO):
    if primeiroArray[i] not in segundoArray:
        diferenca.append(primeiroArray[i])

if len(diferenca) > 0:
    print(f'\nDiferença entre o primeiro e segundo: {diferenca}')
else:
    print(f'\nPrimeiro vetor está contido no segundo.')