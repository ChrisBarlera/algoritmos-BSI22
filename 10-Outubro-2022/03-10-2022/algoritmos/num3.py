from operator import indexOf
import numpy

print('////MAIOR E MENOR E SUAS POSIÇÕES////')

# Declarando estruturas
N = 18

arr = numpy.zeros(N, dtype=int)

# Preenchendo estrutura
print('\nPreencha a estrutura:')
for i in range(N):
    arr[i] = int(input('Número inteiro: '))
print(f'\nEstrutura: {arr}')


# Achando o maior e menor
maior = arr[0]
menor = arr[0]

for i in range(N):
    if arr[i] > maior:
        maior = arr[i]

    if arr[i] < menor:
        menor = arr[i]

# Achando o índice do maior e menor
## indexMaior = indexOf(arr, maior)
## indexMenor = indexOf(arr, menor)
indexMaior = 0
indexMenor = 0
for i in range(N):
    if arr[i] == maior:
        indexMaior = i

    if arr[i] == menor:
        indexMenor = i


# Apresentação
print(f'\nMaior número da estrutura: {maior} | Posição: {indexMaior}')
print(f'Maior número da estrutura: {menor} | Posição: {indexMenor}')