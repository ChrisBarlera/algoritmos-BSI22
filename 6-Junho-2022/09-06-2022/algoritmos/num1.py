# imprimir tabuada de um int de 1 a 10

numDigitado = int(input("Digite um inteiro de 1 a 10: "))

for numero in range(1,11):
    print(f"{numDigitado} x {numero} = {numDigitado * numero}")