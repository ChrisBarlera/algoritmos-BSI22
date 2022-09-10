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

z = []

yTamanhoReal = len(y)-1
for i in range(yTamanhoReal, -1, -1):
    indiceX = yTamanhoReal - i
    produto = x[indiceX] * y[i]
    z.append(produto)

print(z)