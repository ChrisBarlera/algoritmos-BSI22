print("////FIBONACCI////")

limiteFibonacci = int(input("Número limite da sequência: "))

atual = 0
ultimo = 1
penultimo = 0
while True:
    atual = ultimo + penultimo
    penultimo = ultimo
    ultimo = atual
    if atual <= limiteFibonacci:
        print(atual)
    else:
        break