maior = int()
menor = int()

contador = 0
while contador < 3:
    numInserido = int(input("Insira um número: "))
    if contador == 0:
        maior = numInserido
        menor = numInserido
    else:
        if numInserido > maior:
            maior = numInserido
        if numInserido < menor:
            menor = numInserido
    contador += 1
print(f"O menor e maior número digitados (respectivamente) são:{menor,maior}")