print('////Maior e Menor////')

contador = 0
maior = 0
menor = 0
while True:
    print('\n//Digite um inteiro ou 0 para sair do programa//')
    numDigitado = int(input('Int: '))
    if numDigitado == 0:
        break
    else:
        if contador == 0:
            maior = numDigitado
            menor = numDigitado
        elif numDigitado > maior:
            maior = numDigitado
        elif numDigitado < menor:
            menor = numDigitado

        contador += 1

print(f'\nDos {contador} números digitados,')
print(f'o maior e menor foram, respectivamente,')
print(f'Maior:{maior} ; Menor:{menor}')