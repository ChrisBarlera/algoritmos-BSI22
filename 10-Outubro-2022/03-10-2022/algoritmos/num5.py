import numpy

print('////MINIMAX////')

# Declarando estruturas
N = 5
matriz = numpy.zeros((N,N), dtype=int)

# Preenchendo estrutura
print('\nPreencha a matriz')
for i in range(N):
    print(f'Linha {i}')
    for j in range(N):
        matriz[i][j] = int(input('Número inteiro: '))
print('\nMatriz:')
print(matriz)


# Achando o maior número
maior = matriz[0][0]
for i in range(N):
    for j in range(N):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

# Achando linha do maior
linha = 0
for i in range(N):
    for j in range(N):
        if matriz[i][j] == maior:
            linha = i

# Achando menor da linha
menorDaLinha = matriz[linha][0]
for j in range(5):
    if matriz[linha][j] < menorDaLinha:
        menorDaLinha = matriz[linha][j]

# Apresentação
print(f'Elemento minimax: {menorDaLinha}')