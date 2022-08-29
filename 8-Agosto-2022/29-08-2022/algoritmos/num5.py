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

#Juntando as listas numa terceira
z = []
z = x + y

print(f"A junção das litas: {z}")