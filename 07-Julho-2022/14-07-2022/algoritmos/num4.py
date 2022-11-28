print('////Temperaturas////')

contador = 0
maior = 0
menor = 0
soma = 0
media = 0
while True:
    print('\n//Digite a temperatura ou "sair" para sair do programa//')
    numDigitado = input('Temperatura: ')
    if numDigitado.lower() == 'sair':
        break
    else:
        numDigitado = float(numDigitado)
        soma += numDigitado
        if contador == 0:
            maior = numDigitado
            menor = numDigitado
        elif numDigitado > maior:
            maior = numDigitado
        elif numDigitado < menor:
            menor = numDigitado

        contador += 1
        media = soma / contador
        
print(f'\nDos {contador} números digitados,')
print(f'o maior e menor foram,')
print(f'Maior:{maior} ; Menor:{menor}')
print(f'e a média das temperaturas foi {media}')
