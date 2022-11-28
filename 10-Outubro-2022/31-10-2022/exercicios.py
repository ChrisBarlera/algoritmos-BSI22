import os

def criaArquivoSalvaNome(nomeArquivo):
    with open(f"arquivos/{nomeArquivo}.txt", "w") as arquivo:
        nome = input("Digite seu nome: ")
        arquivo.write(nome)

def exercicio1():
    os.system("clear")
    criaArquivoSalvaNome("Exercicio1")

def exercicio2():
    os.system("clear")
    criaArquivoSalvaNome("Exercicio2")

    #Sobrescrevendo o arquivo
    with open("arquivos/Exercicio2.txt", "w") as arquivo:
        arquivo.write("Eu amo algoritmos!")

def exercicio3():
    nome = input("Nome do arquivo: ")

    #Criando arquivo com números digitados
    with open(f"arquivos/{nome}.txt", "w") as arquivo:
        for i in range(5):
            numero = int(input("Número inteiro: "))
            arquivo.write(f"{numero}\n")
    
    lista = []
    with open(f"arquivos/{nome}.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            lista.append(int(linha))
        
    print(f"Lista: {lista}")


def exercicio4():
    #Gravando numero pares e impares em arquivos
    with open("arquivos/impares.txt", "w") as impares, open("arquivos/pares.txt", "w") as pares:
        for n in range(1000):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                impares.write(f"{n}\n")

    with open("arquivos/impares.txt", "r") as impares, open("arquivos/pares.txt", "r") as pares:
        newArquivo = open("arquivos/paresimpares.txt", "w")

        for i in range(500):
            newArquivo.write(pares.readline())
            newArquivo.write(impares.readline())

        # listaPares = pares.readlines()
        # listaImpares = impares.readlines()
 

        # for i in range(500):
        #     newArquivo.write(listaPares[i])
        #     newArquivo.write(listaImpares[i])

def exercicio5():
    with open("arquivos/pares.txt","r") as pares:
        with open("arquivos/paresReverso.txt","w") as paresReverso:
            # tamanho = len(pares.readlines())
            # for i in range(tamanho-1, -1 ,-1):
            #     paresReverso.write(pares.readlines()[i])

            lista_pares = pares.readlines()
            tamanho = len(lista_pares)

            for i in range(tamanho-1,-1,-1):
                paresReverso.write(lista_pares[i])
            

teste = 1
while teste != 0:
    os.system("clear")
    print("MENU DE OPÇÕES:\n 0 - Sair da execução\n 1 - Exercício 1\n 2 - Exercício 2\n 3 - Exercício 3\n 4 - Exercício 4\n 5 - Exercício 5\n")
    teste = int(input("Opção: "))

    if teste == 1:
        exercicio1()
    if teste == 2:
        exercicio2()
    if teste == 3:
        exercicio3()
        input("\nPressione ENTER para continuar: ")

    if teste == 4:
        exercicio4()
    if teste == 5:
        exercicio5()