#Palindromo ou nao?

texto = input('Texto para verificar: ').upper().replace(' ','')

falseCount = 0
for i in range(len(texto)):
    if texto[i] != texto[(i+1)*-1]:
        falseCount += 1

if falseCount == 0:
    print('é palindromo')
else :
    print('nao é palindromo')