import numpy;

print('////GABARITO LOTO////')

arrayR = numpy.zeros(5, dtype=int)
arrayS = numpy.zeros(10, dtype=int)

print('\nGabarito LOTO:')
for i in range(len(arrayR)):
    arrayR[i] = int(input('Número inteiro: '))

print('\nApostas:')
for i in range(len(arrayS)):
    arrayS[i] = int(input('Número inteiro: '))


iguais = []
for i in range(len(arrayS)):
    for j in range(len(arrayR)):
        if arrayS[i] == arrayR[j]:
            iguais.append(arrayR[j])

print(f'\nPontos: {len(iguais)}')            