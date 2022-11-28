import numpy

print('/////SOMA DE LINHAS E COLUNAS/////')

# Declarando matriz
N = 5
matriz = numpy.zeros((N,N), dtype=int)

# Preenchendo matriz 1
print('\n//PREENCHENDO MATRIZ//')
for i in range(N):
    print(f'Linha {i+1}')
    for j in range(N):
        matriz[i][j] = int(input('Digite um inteiro: '))

print('\nSua matriz sem alterações:')
print(matriz)


# Preparando para as somas
somaLinhas = numpy.zeros(N, dtype=int)
somaColunas = numpy.zeros(N, dtype=int)

# somaLinhas = [linha1, linha2, linha3, linha4, linha5]
# somaColunas = [coluna1, coluna2, coluna3, coluna4, coluna5]


# Somando e adicionando aos vetores
for i in range(N):
    for j in range(N):
        somaLinhas[i] += matriz[i][j]
        somaColunas[i] += matriz[j][i]

# Mostrando
print(f'\nSoma das linhas: {somaLinhas}')
print(f'Soma das colunas: {somaColunas}')
