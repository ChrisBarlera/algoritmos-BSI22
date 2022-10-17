print('////ÁREA DE UM QUADRADO////')

def Area_quadrado(lado):
    return lado * lado

lado = float(input('\nDigite o lado do quadrado: '))
area = Area_quadrado(lado)

print(f'\nÁrea do quadrado : {area}')