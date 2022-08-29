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
for i in range(len(y)-1, -1, -1):
    indiceX = len(y) -1 - i
    produto = x[indiceX] * y[i]
    z.append(produto)

print(z)