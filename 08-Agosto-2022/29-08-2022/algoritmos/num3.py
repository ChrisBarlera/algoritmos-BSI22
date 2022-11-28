x = []
y = []

tamanhoListas = 5

# Preenchendo a lista x com dados do usuário
print("//Lista X//")
for i in range(tamanhoListas):
    x.append(int(input("Número inteiro: ")))


# Preenchendo a lista y com dados do usuário
print("\n//Lista Y//")
for i in range(tamanhoListas):
    y.append(int(input("Número inteiro: ")))

# Somando a lista x
somaX = 0
for num in x:
    somaX += num

# Somando a lista y
somaY = 0
for num in y:
    somaY += num

somaTotal = somaX + somaY

print(f"Valor da soma das duas listas: {somaTotal}")
