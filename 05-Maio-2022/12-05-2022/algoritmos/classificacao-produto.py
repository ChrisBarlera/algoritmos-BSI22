codigo = int(input("Código do produto: "))

if codigo == 1:
    classificao = "Alimento não-perecível"
elif codigo == 2 or codigo == 3 or codigo == 4:
    classificao = "Alimento perecível"
elif codigo == 5 or codigo == 6:
    classificao = "Vestuário"
elif codigo == 7:
    classificao = "Higiene pessoal"
elif codigo >= 8 and codigo <= 15:
    classificao = "Limpeza e utensílios domésticos"
else:
    classificao = "Inválido"

print(classificao)