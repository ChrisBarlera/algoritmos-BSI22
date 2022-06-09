#Informar um inteiro e indicar se é primou ou não

numDigitado = int(input("Digite um inteiro: "))
whileCont = 10
qtdDivExatas = 0
while (whileCont > 0):
    if numDigitado % whileCont == 0:
        qtdDivExatas += 1
    whileCont -= 1

if qtdDivExatas == 2:
    print("Número é primo")
else:
    print("Número não é primo")