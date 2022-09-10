import numpy

print('////INTERCALANDO VETORES////')

TAMANHO = 5

primeiroArray = numpy.zeros(TAMANHO, dtype=int)
segundoArray = numpy.zeros(TAMANHO, dtype=int)

print('\nPrimeiro vetor:')
for i in range(TAMANHO):
    primeiroArray[i] = int(input('Número inteiro: '))

print('\nSegundo vetor:')
for i in range(TAMANHO):
    segundoArray[i] = int(input('Número inteiro: '))        

#Preenchendo lista intercalada:
intercalados = []
arraysCont = 0
for i in range(TAMANHO * 2):
    if i % 2 == 0:
        intercalados.append(primeiroArray[arraysCont])
        arraysCont+=1
    else:
        intercalados.append(segundoArray[arraysCont-1])
        

print(f'\nResultado da intercalação: \n{intercalados}')