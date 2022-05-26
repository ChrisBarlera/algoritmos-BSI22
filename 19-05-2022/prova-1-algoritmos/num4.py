# Aluno: Christian Honorato Barlera de Andrade
# Turma: BSI22

# Capacidade elevador e peso de 5 pessoas.

capacidade = float(input("Capacidade total do elevador: "))
pessoa1 = float(input("Peso da pessoa 1: "))
pessoa2 = float(input("Peso da pessoa 2: "))
pessoa3 = float(input("Peso da pessoa 3: "))
pessoa4 = float(input("Peso da pessoa 4: "))
pessoa5 = float(input("Peso da pessoa 5: "))

pesoTotalPessoas = pessoa1 + pessoa2 + pessoa3 + pessoa4 + pessoa5

if pesoTotalPessoas > capacidade:
    print("Capacidade do elevador excedida")
else:
    print("Elevador está liberado para uso")