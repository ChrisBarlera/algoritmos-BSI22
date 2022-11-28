from pickletools import string1


string1 = input('String1: ')
string2 = input('String2: ')

if string2 in string1:
    print(f'Segunda esta na primeira, na posicao {string1.find(string2)}')
else:
    print('Segunda nao esta na primeira')