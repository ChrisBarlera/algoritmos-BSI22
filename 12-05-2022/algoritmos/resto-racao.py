pesoSaco = float(input("Peso do saco (em Kg):"))
qtdDiaria = float(input("Quantidade para cada gato (em gramas):"))
qtdDiaria = (qtdDiaria / 1000) * 2

numeroDias = 5
pesoSaco = pesoSaco - (qtdDiaria * numeroDias)

print("\n/////////////////////////////////\n")
print("O resto no saco (em Kg) após 5 dias é:",pesoSaco)