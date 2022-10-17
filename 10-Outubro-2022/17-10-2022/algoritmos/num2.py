def impares_intervalo_1_ate_n(n):
    if n > 1:
        print("\nÍmpares do intervalo até o número:")
        for i in range(1, n+1):
            if i % 2 != 0:
                print(i)
    else:
        print("Valor inserido inválido")

x = int(input("Digite um inteiro: "))
impares_intervalo_1_ate_n(x)