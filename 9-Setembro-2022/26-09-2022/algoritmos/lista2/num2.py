import numpy

print('/////TROCA DE VALORES/////')

# Declarando matriz
N = 10

matriz = numpy.zeros((N,N), dtype=int)

# Preenchendo matriz 1
print('\n//PREENCHENDO MATRIZ//')
for i in range(N):
    print(f'Linha {i+1}')
    for j in range(N):
        matriz[i][j] = int(input('Digite um inteiro: '))

print('\nSua matriz sem alterações:')
print(matriz)

# Apanhando os valores das linhas e colunas
tempLinha2 = []
tempLinha8 = []
tempLinha5 = []
tempColuna9 = []

for i in range(N):
    for j in range(N):
        if i == 1:
            tempLinha2.append(matriz[i][j])
        if i == 7:
            tempLinha8.append(matriz[i][j])
        if i == 4:
            tempLinha5.append(matriz[i][j])
        if j == 8:
            tempColuna9.append(matriz[i][j])

# Realizando as trocas
for i in range(N):
    for j in range(N):
        if i == 1:
            matriz[i][j] = tempLinha8[j]
        if i == 7:
            matriz[i][j] = tempLinha2[j]
        if i == 4:
            matriz[i][j] = tempColuna9[j]
        if j == 8:
            matriz[i][j] = tempLinha5[j]

print('\nSua matriz com valores trocados:')
print(matriz)