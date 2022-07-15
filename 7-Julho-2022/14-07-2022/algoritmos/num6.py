print('/////Contando nos intervalos//////')
print('//Digite um número inteiro//')
print('//Caso o número seja negativo, o programa vai parar//')

contA = 0 #Intervalo [0-25]
contB = 0 #Intervalo [26-50]
contC = 0 #Intervalo [51-75]
contD = 0 #Intervalo [76-100]

while True:
    numDigitado = int(input('Int: '))
    if numDigitado < 0:
        break
    else:
        if numDigitado >= 0 and numDigitado <= 25:
            contA += 1
        if numDigitado >= 26 and numDigitado <= 50:
            contB += 1
        if numDigitado >= 51 and numDigitado <= 75:
            contC += 1
        if numDigitado >= 76 and numDigitado <= 100:
            contD += 1

print(f'\nIntervalo[0-25]: {contA} números')
print(f'Intervalo[26-50]: {contB} números')
print(f'Intervalo[51-75]: {contC} números')
print(f'Intervalo[76-100]: {contD} números')
