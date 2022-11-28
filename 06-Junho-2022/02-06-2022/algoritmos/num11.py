contador = 0
qtdMaior30 = 0

while contador < 15:
    numDigitado = float(input("Digite um número: "))
    if numDigitado > 30:
        qtdMaior30 += 1
    contador += 1
print("Quantidade de números maiores que 30:",qtdMaior30)