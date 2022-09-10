print('////MODELOS E CONSUMOS DE CARROS////')

modelosCarros = []
consumosCarros = []

TAMANHO = 5

print('\nLista de modelos dos carros:')
for i in range(TAMANHO):
    modelosCarros.append(input('Modelo: '))

print('\nLista do consumo desses carros (em Km/L): ')
for i in range(TAMANHO):
    consumosCarros.append(float(input(f'Consumo do {modelosCarros[i]}: ')))

#Achando o mais econômico:
economico = consumosCarros[0]
economicoIndex = 0
for i in range(TAMANHO):
    if consumosCarros[i] > economico:
        economico = consumosCarros[i]
        economicoIndex = i

print((f'O carro mais econômico é o {modelosCarros[economicoIndex]}'))

print('\nMostrando o consumo em 1000Km')
for i in range(TAMANHO):
    print(f'{modelosCarros[i]} consome {1000 / consumosCarros[i]} litros em 1000Km')