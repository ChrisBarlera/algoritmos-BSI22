nome = input("Insira o nome do aluno: ")
nota1 = float(input("Nota 1 do aluno (peso 2): "))
nota2 = float(input("Nota 2 do aluno (peso 3): "))
print("Média ponderada do aluno:",(nota1 * 2 + nota2 * 3)/(2+3))