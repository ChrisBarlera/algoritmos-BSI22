precoFabrica = float(input("Preço de fábrica: "))
prcntLucro = float(input("Percentual de lucro: "))
prcntImpostos = float(input("Percentual de impostos: "))

valorLucro = precoFabrica * prcntLucro/100
valorImpostos = precoFabrica * prcntImpostos/100
valorFinal = precoFabrica + valorLucro + valorImpostos
print("\n//////////////////\n")
print("Lucro do distribuidor:",valorLucro)
print("Impostos:",valorImpostos)
print("Valor final do consumidor:",valorFinal)