# Sabe-se que:
# 1 Pé =12 polegadas
# 1 jarda = 3 pés
# 1 milha = 1760 jardas
# Faça um programa que receba uma medida em pés, faça as conversões e a seguir
# mostre os resultados em:
    # a) Polegadas
    # b) Jardas
    # c) Milhas

medida_pes = float(input("Medida em pés a ser convertida: "))
polegadas = medida_pes * 12
jardas = medida_pes / 3
milhas = jardas / 1760
print("Polegadas:",polegadas,"\nJardas:",jardas,"\nMilhas:",milhas)