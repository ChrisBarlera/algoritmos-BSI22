intA = int(input("Int A: "))
intB = int(input("Int B: "))
intC = int(input("Int C: "))


#Achando o menor termo
menor = intA
if intB < menor:
    menor = intB
if intC < menor:
    menor = intC

#Achando o maior termo
maior = intA
if intB > maior:
    maior = intB
if intC > maior:
    maior = intC

#Achando o intermediário
intermediario = intA
if intA > menor and intA < maior:
    intermediario = intA
if intB > menor and intB < maior:
    intermediario = intB
if intC > menor and intC < maior:
    intermediario = intC

print(f"Valor intermediário: {intermediario}")