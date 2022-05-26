# Aluno: Christian Honorato Barlera de Andrade
# Turma: BSI22

# Tres ints diferentes e apresentar o valor intermediário.

a = int(input("int A: "))
b = int(input("int B: "))
c = int(input("int C: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

menor = b
if a < menor:
    menor = a
if c < menor:
    menor = c

if a > menor and a < maior:
    intermedio = a
elif b > menor and b < maior:
    intermedio = b
else:
    intermedio = c

print("\nMaior:",maior)
print("Intermediário:",intermedio)
print("Menor:",menor)