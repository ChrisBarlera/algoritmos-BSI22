from operator import le


x = []

tamanho = 2

# Preenchendo a lista com dados do usuário
for i in range(tamanho):
    x.append(int(input("Número inteiro: ")))

for i in range(len(x)):
    if x[i] % 2 == 0:
        x[i] = x[i] * i
    else:
        x[i] = i

print(f"Valores armazenados: {x}")