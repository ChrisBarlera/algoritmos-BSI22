import numpy;

print('////ELEMENTOS COMUNS ENTRE DOIS ARRAYS////')

arrayR = numpy.zeros(5, dtype=int)
arrayS = numpy.zeros(10, dtype=int)

print('\nPreencha o vetor R')
for i in range(len(arrayR)):
    arrayR[i] = int(input('Número inteiro: '))

print('\nPreencha o vetor S')
for i in range(len(arrayS)):
    arrayS[i] = int(input('Número inteiro: '))


iguais = []
# for i in range(len(arrayS)):
#     for j in range(len(arrayR)):
#         if arrayS[i] == arrayR[j]:
#             iguais.append(arrayR[j])

for num in arrayS:
    if num in arrayR:
        iguais.append(num)

print(f'\nItens iguais nos vetores: {iguais}')            