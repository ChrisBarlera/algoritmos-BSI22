# Alguns países medem temperaturas em graus Celsius, e outros em graus
# Fahrenheit. Faça um algoritmo para ler uma temperatura Celsius e imprimi-la
# em Fahrenheit (pesquise como fazer este tipo de conversão).

celsius = float(input("Temperatura em Celsius: "))
fahrenheit = ((9 * celsius)/5) + 32
print("Temperatura convertida para Fahrenheit:",fahrenheit)