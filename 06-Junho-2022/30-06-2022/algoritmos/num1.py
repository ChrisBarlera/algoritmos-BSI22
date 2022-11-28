nome = input("Nome: ")
nome = nome.upper()
nomeInvertido = list(nome)

for i in range(len(nome)-1, -1, -1):
    nomeInvertido[len(nome)-1 -i] = nome[i]

print(str().join(nomeInvertido))


#/////////////V2///////
# nome = input("Nome: ")
# nome = nome.upper()
# print(nome[::-1])