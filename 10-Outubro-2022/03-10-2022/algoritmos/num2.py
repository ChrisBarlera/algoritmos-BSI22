import numpy

print('////NEGATIVOS E SUAS POSIÇÕES////')

# Declarando estruturas
N = 10

arr = numpy.zeros(N, dtype=int)
negativos = []
negativosIndexes = []

# Preenchendo estrutura
print('\nPreencha a estrutura:')
for i in range(N):
    arr[i] = int(input('Número inteiro: '))
print(f'\nEstrutura: {arr}')


# Achando os negativos
for i in range(N):
    if arr[i] < 0:
        negativos.append(arr[i])
        negativosIndexes.append(i)


# Apresentação
if len(negativos) > 0:
    print('\nOs negativos são:')
    for i in range(len(negativos)):
        print(f'Número: {negativos[i]} | Posição na estrutura original: {negativosIndexes[i]}')
else:
    print('\nNão existem números negativos na estrutura')