#O usuário sempre informará uma data válida, não sendo necessário fazer este teste;
#Considere que os anos são todos não-bissextos
#Considere que todo mes tem 30 dias

print("Informe uma data inicial")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))

diasPassados = int(input("\nAgora, informe quantos dias deseja somar à data: "))

if diasPassados >= 365:
    somaAnos = diasPassados // 365
    ano = ano + somaAnos
    diasPassados = diasPassados % 365

if(diasPassados >= 30):
    somaMes = diasPassados // 30
    mes = mes + somaMes
    diasPassados = diasPassados % 30


# ///////// CODIGO ABANDONADO (TENTATIVA DE CONSIDERAR A QUANTIDADE DE DIAS CERTOS DE CADA MES)
# if diasPassados >= 28:
#     if mes == 2:
#         qtd_DiasdoMes = 28
#         if dia+diasPassados <= qtd_DiasdoMes:
#             dia = dia + diasPassados
#         else:
#             dia = (dia + diasPassados) - qtd_DiasdoMes
#             mes = mes + 1

#     elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
#         qtd_DiasdoMes = 31
#         if dia+diasPassados <= qtd_DiasdoMes:
#             dia = dia + diasPassados
#         else:
#             if mes == 12:
#                 dia = (dia + diasPassados) - qtd_DiasdoMes
#                 mes = 1
#                 ano = ano + 1
#             else: 
#                 dia = (dia + diasPassados) - qtd_DiasdoMes
#                 mes = mes + 1
                
#     else:
#         qtd_DiasdoMes = 30
#         if dia+diasPassados <= qtd_DiasdoMes:
#             dia = dia + diasPassados
#         else:
#             dia = (dia + diasPassados) - qtd_DiasdoMes
#             mes = mes + 1

print(f"Nova data:{dia+diasPassados,mes,ano}")