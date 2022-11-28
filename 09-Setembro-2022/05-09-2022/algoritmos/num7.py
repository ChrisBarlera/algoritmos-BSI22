import numpy

print('////DIFERENÇA DE VETORES////')

TAMANHO = 3

primeiroArray = numpy.zeros(TAMANHO, dtype=int)
segundoArray = numpy.zeros(TAMANHO, dtype=int)

print('\nPrimeiro vetor (X):')
for i in range(TAMANHO):
    primeiroArray[i] = int(input('Número inteiro: '))

print('\nSegundo vetor (Y):')
for i in range(TAMANHO):
    segundoArray[i] = int(input('Número inteiro: '))

#Montando a lista de diferença
diferenca = []
for i in range(TAMANHO):
    if primeiroArray[i] not in segundoArray:
        diferenca.append(primeiroArray[i])

if len(diferenca) > 0:
    print(f'\nDiferença entre o primeiro e segundo (X-Y): {diferenca}')
else:
    print(f'\nPrimeiro vetor está contido no segundo. (X em Y)')