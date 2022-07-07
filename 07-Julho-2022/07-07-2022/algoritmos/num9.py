from operator import le


frase = input('Uma frase: ')

lista = frase.split(' ')

for element in lista:
    if element == '':
        lista.remove(element)

print(f'Numero de palavras: {len(lista)}')