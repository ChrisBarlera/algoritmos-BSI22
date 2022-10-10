print('////MAIOR NÚMERO ENTRE DOIS////')

def Maximo(a,b):
    if a >= b:
        return a
    elif b >= a:
        return b

num1 = int(input('\nDigite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))

maior = Maximo(num1,num2)

print(f'\nO maior é: {maior}')