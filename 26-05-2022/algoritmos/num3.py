a = int(input("Inteiro A: "))
b = int(input("Inteiro B: "))
c = int(input("Inteiro C: "))
d = int(input("Inteiro D: "))
e = int(input("Inteiro E: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d
if e > maior:
    maior = e

print("Maior número:",maior)