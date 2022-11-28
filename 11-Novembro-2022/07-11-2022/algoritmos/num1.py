def getNomes(tabela):
    nomes = []
    for i in range(len(tabela)):
        nomes.append(int(tabela[i][0]))
    
    return nomes

def getNumeros(tabela):
    numeros = []
    for i in range(len(tabela)):
        numeros.append(int(tabela[i][1]))
    
    return numeros

def bytesParaMB(bytes):
    megabyte = bytes/1024**2
    megabyte = "{:.2f}".format(megabyte)
    return megabyte

def conversao(tabela):
    lista = getNumeros(tabela)
    for numero in lista:
        print(bytesParaMB(numero))


# Gerando lista de lista com os dados do texto
tabela = []
with open("../arquivos/usuarios.txt", "r") as usuarios:
    linhas = usuarios.readlines()
    for i in range(len(linhas)):
        tabela.append(linhas[i].split())


conversao(tabela)
# with open("../arquivos/relatorio.txt", "w") as relatorio:
#     for i in range(len(tabela)):
#         for j in range(2):
#             print()