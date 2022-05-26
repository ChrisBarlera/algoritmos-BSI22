print("Informe uma data inicial")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))

diasPassados = int(input("\nAgora, informe quantos dias deseja somar à data: "))

if diasPassados >= 365:
    somaAnos = diasPassados // 365
    ano = ano + somaAnos
    diasPassados = diasPassados % 365

if diasPassados >= 28:
    if mes == 2:
        qtd_DiasdoMes = 28
        if dia+diasPassados <= qtd_DiasdoMes:
            dia = dia + diasPassados
        else:
            dia = (dia + diasPassados) - qtd_DiasdoMes
            mes = mes + 1

    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        qtd_DiasdoMes = 31
        if dia+diasPassados <= qtd_DiasdoMes:
            dia = dia + diasPassados
        else:
            if mes == 12:
                dia = (dia + diasPassados) - qtd_DiasdoMes
                mes = 1
                ano = ano + 1
            else: 
                dia = (dia + diasPassados) - qtd_DiasdoMes
                mes = mes + 1
                
    else:
        qtd_DiasdoMes = 30
        if dia+diasPassados <= qtd_DiasdoMes:
            dia = dia + diasPassados
        else:
            dia = (dia + diasPassados) - qtd_DiasdoMes
            mes = mes + 1

print(f"Nova data:{dia,mes,ano}")