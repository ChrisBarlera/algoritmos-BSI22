contador = 0
qtdNegativos = 0
soma = 0
while contador < 3:
    numDigitado = float(input("Digite um número: "))
    if numDigitado < 0:
        qtdNegativos += 1
    else:
        soma = soma + numDigitado
    contador += 1
print(f"Quantidade de negativos:{qtdNegativos}\nSoma dos positivos:{soma}")