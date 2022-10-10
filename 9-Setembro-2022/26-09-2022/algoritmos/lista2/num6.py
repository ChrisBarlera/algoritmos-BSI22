import numpy

print('/////MULTIPLICAÇÃO POR UM VETOR/////')

# Declarando matriz
N = 5
vetor = numpy.zeros(N, dtype=int)
matriz = numpy.zeros((N,N), dtype=int)

# Preenchendo o vetor multiplicador
print('\n//PREENCHENDO VETOR//')
for i in range(N):
    vetor[i] = int(input('Digite um inteiro: '))

print(f'\nSeu vetor: {vetor}')

# Preenchendo matriz
print('\n//PREENCHENDO MATRIZ//')
for i in range(N):
    print(f'Linha {i+1}')
    for j in range(N):
        matriz[i][j] = int(input('Digite um inteiro: '))

print('\nSua matriz sem alterações:')
print(matriz)


# Fazendo as multiplicações
for i in range(N):
    for j in range(N):
        matriz[i][j] *= vetor[i]

# Apresentando
print('\nSua matriz multiplicada:')
print(matriz)