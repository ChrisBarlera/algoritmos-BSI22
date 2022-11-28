import numpy

print('/////DETERMINANTE DE MATRIZ 2x2/////')

# Declarando matriz
N = 2
matriz = numpy.zeros((N,N), dtype=int)

# Preenchendo matriz
print('\n//PREENCHENDO MATRIZ 1//')
for i in range(N):
    print(f'Linha {i+1}')
    for j in range(N):
        matriz[i][j] = int(input('Digite um inteiro: '))

print('\nSua matriz:')
print(matriz)


# Achando diagonal principal e secundária
diagPrincipal = []
diagSecundaria = []
for i in range(N):
    for j in range(N):
        if i == j:
            diagPrincipal.append(matriz[i][j])
        if i + j == N - 1: 
            diagSecundaria.append(matriz[i][j])

# Calculando determinante
principalMultiplicada = 0
secundariaMultiplicada = 0
for i in range(N):
    if i == 0:
        principalMultiplicada = diagPrincipal[i]
        secundariaMultiplicada = diagSecundaria[i]
    else:
        principalMultiplicada *= diagPrincipal[i]
        secundariaMultiplicada *= diagSecundaria[i]
        
determinante = principalMultiplicada + (secundariaMultiplicada * -1)

print(f'\nO determinante é: {determinante}')