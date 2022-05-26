idade = int(input("Idade: "))
sexo = input("Sexo(M ou F): ")

if sexo == "F":
    if idade < 12:
        print("Menina")
    elif idade >= 12 and idade <=24:
        print("Moça")
    else:
        print("Mulher")
else:
    if idade < 12:
        print("Menino")
    elif idade >= 12 and idade <=24:
        print("Rapaz")
    else:
        print("Homem")