from operator import le


texto = input("String: ").upper()

for i in range(len(texto)):
    if texto[i] not in texto[0:i]:
        print(f'{texto[i]}: {texto.count(texto[i])}x')