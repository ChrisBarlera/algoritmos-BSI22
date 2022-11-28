frase = input("Digite uma frase: ")
frase = frase.upper()

qtdEspacos = frase.count(" ")
qtdVogalA = frase.count("A")
qtdVogalE = frase.count("E")
qtdVogalI = frase.count("I")
qtdVogalO = frase.count("O")
qtdVogalU = frase.count("U")
qtdVogalTotal = qtdVogalA + qtdVogalE + qtdVogalI + qtdVogalO + qtdVogalU

print(f"Quantidade de espaços em branco: {qtdEspacos}")
print(f"Quantas vezes aparece a voga 'a': {qtdVogalA}")
print(f"Quantas vezes aparece a voga 'e': {qtdVogalE}")
print(f"Quantas vezes aparece a voga 'i': {qtdVogalI}")
print(f"Quantas vezes aparece a voga 'o': {qtdVogalO}")
print(f"Quantas vezes aparece a voga 'u': {qtdVogalU}")
print(f"Quantidade total de vogais: {qtdVogalTotal}")