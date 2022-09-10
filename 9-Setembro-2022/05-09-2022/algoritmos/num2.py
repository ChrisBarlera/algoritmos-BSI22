import numpy

print("////PRIMOS E SUAS POSIÇÕES////")

TAMANHO = 2

vetor = numpy.zeros(TAMANHO, dtype=int)

#Preenche o vetor
for i in range(TAMANHO):
    vetor[i] = int(input("Número inteiro: "))

#Passa pelo vetor fazendo a verificação
for num in vetor:
    qtdDivExatas = 0
    for i in range(1, num):
        if num % i == 0:
            qtdDivExatas+=1
    if qtdDivExatas == 2:
        print(f"")
    else:
        print("Número não é primo")
# while (whileCont > 0):
#     if numDigitado % whileCont == 0:
#         qtdDivExatas += 1
#     whileCont -= 1
