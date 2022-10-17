def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                soma += matriz[i][j]
    return soma


matriz =   [[1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4]]
            
print(soma_diagonal_principal(matriz))