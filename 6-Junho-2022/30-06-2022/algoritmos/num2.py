nome = input("Nome: ")
nome = nome.upper()

for i in range(len(nome)):
    print(nome[0:i+1])