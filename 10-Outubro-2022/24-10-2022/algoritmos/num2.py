def somaDeElementosMatriz(matriz):
    soma = 0
    # for i in range(len(matriz)):
    #     for j in range(len(matriz)):
    #         soma += matriz[i][j]
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    
    return soma


matriz =    [[1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5]]

somaMatriz = somaDeElementosMatriz(matriz)
print(f'A soma de todos os elementos da matriz é: {somaMatriz}')