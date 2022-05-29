a = int(input("Inteiro A: "))
b = int(input("Inteiro B: "))
c = int(input("Inteiro C: "))

menor = a
if b < menor:
    menor = b
elif c < menor:
    menor = c

maior = b
if a > maior:
    maior = a
elif c > maior:
    maior = c

if a > menor and a < maior:
    intermedio = a
elif b > menor and b < maior:
    intermedio = b
else:
    intermedio = c

print(f"{menor,intermedio,maior}")