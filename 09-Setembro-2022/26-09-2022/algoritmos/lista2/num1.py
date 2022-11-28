import numpy

print("/////SOMA DAS MATRIZES/////")

# Declarando matriz
N = int(input('Dimensão das matrizes quadradas: '))

m1 = numpy.zeros((N,N), dtype=int)
m2 = numpy.zeros((N,N), dtype=int)

# Preenchendo matriz 1
print('\n//PREENCHENDO MATRIZ 1//')
for i in range(N):
    print(f'Linha {i+1}')
    for j in range(N):
        m1[i][j] = int(input('Digite um inteiro: '))
print(f'\n{m1}')

# Preenchendo matriz 2
print('\n//PREENCHENDO MATRIZ 2//')
for i in range(N):
    print(f'Linha {i+1}')
    for j in range(N):
        m2[i][j] = int(input('Digite um inteiro: '))
print(f'\n{m2}')


# Fazendo a soma
resultante = numpy.zeros((N,N), dtype=int)
for i in range(N):
    for j in range(N):
        resultante[i][j] = m1[i][j] + m2[i][j]


print('\nMatriz resultante da soma:')
print(resultante)