def diferencaA_menos_B(lista_A, lista_B):
    A = set(lista_A)
    B = set(lista_B)

    print(f'Elementos que estão em A mas não em B: {A-B}')

l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = [1,2,3,4,5,6,7,8,9,10]

diferencaA_menos_B(l1, l2)