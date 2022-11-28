anoNasc = int(input("Ano de nascimento: "))
anoAtual = 2022
idade = anoAtual - anoNasc
if idade >= 16:
    print("Pode Votar!")
    if idade >= 18:
        print("Também pode tirar CNH!!")
    else:
        print("Mas não pode tirar CNH :(")
else:
    print("Não pode votar nem tirar CNH")