# fatorial de um inteiro

numDigitado = int(input("Digite um inteiro: "))
fatorial = 1
for numero in range(numDigitado,0,-1):
    fatorial = fatorial * numero

print(fatorial)