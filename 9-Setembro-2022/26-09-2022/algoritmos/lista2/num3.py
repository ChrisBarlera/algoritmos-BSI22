import numpy

print('/////MULTIPLICAÇÃO POR UM NÚMERO/////')

# Declarando matriz
N = 4
matriz = numpy.zeros((N,N))

# Preenchendo matriz 1
print('\n//PREENCHENDO MATRIZ//')
for i in range(N):
    print(f'Linha {i+1}')
    for j in range(N):
        matriz[i][j] = float(input('Digite um número: '))

print('\nSua matriz sem alterações:')
print(matriz)


# Preparando para a multiplicação
valorA = float(input('\nDigite um valor para multiplicar os índices: '))
valoresMultiplicados = []

# Multiplicando e adicionando à lista
for i in range(N):
    for j in range(N):
        valoresMultiplicados.append(matriz[i][j] * valorA)

# Mostrando
print(f'\nO resultado dos valores multiplicados: {valoresMultiplicados}')