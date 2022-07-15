print('////Valores I, A, B, e C////')

valorI = int(input("I: "))
valorA = float(input("A: "))
valorB = float(input("B: "))
valorC = float(input("C: "))

menor = 0
medio = 0
maior = 0

#Descobrindo os menores
if valorA < valorB and valorA < valorC:
    menor = valorA
if valorB < valorA and valorB < valorC:
    menor = valorB
if valorC < valorA and valorC < valorB:
    menor = valorC

#Descobrindo os maiores
if valorA > valorB and valorA > valorC:
    maior = valorA
if valorB > valorA and valorB > valorC:
    maior = valorB
if valorC > valorA and valorC > valorB:
    maior = valorC

#Descobrindo os medios
if valorA > menor and valorA < maior:
    medio = valorA
if valorB > menor and valorB < maior:
    medio = valorB
if valorC > menor and valorC < maior:
    medio = valorC

if valorI == 1:
    print('Os números A, B e C em ordem crescente:')
    print(f'{menor}; {medio}; {maior}')

if valorI == 2:
    print('Os números A, B e C em ordem deccrescente:')
    print(f'{maior}; {medio}; {menor}')
    