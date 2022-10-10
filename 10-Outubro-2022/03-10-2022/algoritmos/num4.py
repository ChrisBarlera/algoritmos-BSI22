import numpy

print('////TROCANDO COLUNA POR VETOR////')

# Declarando estruturas
vetor = numpy.zeros(3, dtype=int)
matriz = numpy.zeros((3,4), dtype=int)
coluna1_original = []

# Preenchendo estruturas
print('\nPreencha o vetor:')
for i in range(3):
    vetor[i] = int(input('Número inteiro: '))
print(f'\nVetor: {vetor}')

print('\nPreencha a matriz')
for i in range(3):
    print(f'Linha {i}')
    for j in range(4):
        matriz[i][j] = int(input('Número inteiro: '))
print('\nMatriz:')
print(matriz)

# Recolhendo valor da coluna 1 e já trocando para valor do vetor
for i in range(3):
    for j in range(4):
        if j == 1:
            coluna1_original.append(matriz[i][j])
            matriz[i][j] = vetor[i]

# Substituindo valores do vetor
for i in range(3):
    vetor[i] = coluna1_original[i]

# Apresentação
print('\nVetor alterado: ')
print(vetor)

print('\nMatriz alterada: ')
print(matriz)