# Aluno: Christian Honorato Barlera de Andrade
# Turma: BSI22

# Receber int e dizer se é positivo ou não.

num = int(input("Digite um número inteiro: "))

if num < 0:
    print("Número digitado é negativo")
elif num == 0:
    print("Número digitado é nulo")
else:
    print("Número digitado é positivo")