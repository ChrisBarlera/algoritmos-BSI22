matricula = input("Matrícula do aluno: ")
prova1 = float(input("Prova 1: "))
prova2 = float(input("Prova 2: "))
prova3 = float(input("Prova 3: "))
exercicios = float(input("Exercícios: "))

media = (prova1*1 + prova2*2 + prova3*2 + exercicios*1)/(1+2+2+1)

if media >= 9:
    conceito = "A"
if media >= 7.5:
    conceito = "B"
if media >= 6:
    conceito = "C"
if media >= 4:
    conceito = "D"
if media < 4:
    conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
    situacao = "Aprovado :)"
if conceito == "D" or conceito == "E":
    situacao = "Reprovado :("
print("\nAluno:",matricula,"\nConceito:",conceito,"\nSituação:",situacao)