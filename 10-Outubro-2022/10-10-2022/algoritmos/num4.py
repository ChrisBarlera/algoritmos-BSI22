print('////ÁREA DE UM TRIÂNGULO////')

def Area_triangulo(base:float, altura:float) -> float:
    area = (base * altura) / 2
    return area

base = float(input('\nTamanho da base do triângulo: '))
altura = float(input('\nTamanho da altura do triângulo: '))

area = Area_triangulo(base, altura)

print(f'\nÁrea do triângulo : {area}')