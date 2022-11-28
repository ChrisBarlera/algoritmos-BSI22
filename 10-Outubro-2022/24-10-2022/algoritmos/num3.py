def substituirNegativos(V):
    for i in range(len(V)):
        if V[i] < 0:
            V[i] = 0


lista = []
for i in range(-5,20):
    lista.append(i)

print(f'Vetor usado: {lista}')

substituirNegativos(lista)

print(f'Vetor modificado: {lista}')