print('////NÚMERO IMPAR OU PAR////')

def e_par(x):
    if x % 2 == 0:
        return True
    else:
        return False

numero = int(input('\nDigite um número inteiro: '))

print(f'\nO número é par? : {e_par(numero)}')