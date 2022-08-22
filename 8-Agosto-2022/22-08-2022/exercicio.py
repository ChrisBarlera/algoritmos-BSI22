#Leia 10 valores --
#armazene em um array X --
#exiba os valores --
#apresente o somatório dos valores --
#apresente a média dos valores --
#apresente o maior e menor valor --
#apresente os indices do maior e menor valor --

import numpy

#Inicializa o vetor
LEN = 10
vetorX = numpy.zeros(LEN)

#Atribui os valores
for i in range(LEN):
    vetorX[i] = float(input("Número: "))

#Exibe os valores
print(f"Vetor: {vetorX}")

#soma os valores
soma = 0
for i in range(LEN):
    soma += vetorX[i]

#Exibe a soma
print(f"Soma: {soma}")

#Calcula e exibe média
media = soma / LEN
print(f"Média {media}")

#Acha o maior valor
maior = vetorX[0]
for i in range(LEN):
    if vetorX[i] > maior:
        maior = vetorX[i]
print(f"Maior valor: {maior}")

#Acha o menor valor
menor = vetorX[0]
for i in range(LEN):
    if vetorX[i] < menor:
        menor = vetorX[i]
print(f"Menor valor: {menor}")

#Acha o índice do maior
maiorIndex = 0
for i in range(LEN):
    if maior == vetorX[i]:
        maiorIndex = i
print(f"Índice do maior: {maiorIndex}")

#Acha o índice do menor
menorIndex = 0
for i in range(LEN):
    if menor == vetorX[i]:
        menorIndex = i
print(f"Índice do menor: {menorIndex}")