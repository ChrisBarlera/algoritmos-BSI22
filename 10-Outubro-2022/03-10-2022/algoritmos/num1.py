import numpy

print('////ESTRUTURA EM ORDEM INVERSA////')

# Declarando estruturas
N = 3

arrA = numpy.zeros(N, dtype=int)
arrB = numpy.zeros(N, dtype=int)
invA = []
invB = []

# Preenchendo estrutura
print('\nEstrutura A')
for i in range(N):
    arrA[i] = int(input('Número inteiro: '))
print(f'Estrutura: {arrA}')

print('\nEstrutura B')
for i in range(N):
    arrB[i] = int(input('Número inteiro: '))
print(f'Estrutura: {arrB}')


# Montando a lista com os arrays invertidos
for i in range(N-1, -1, -1):
    invA.append(arrA[i])
    invB.append(arrB[i])

# Apresentação
print(f'Estrutura A invertida: {invA}')
print(f'Estrutura B invertida: {invB}')
