valor_etiqueta = float(input("Valor do produto: "))
codigo_pagamento = int(input("Código do tipo de pagamento: "))
if codigo_pagamento == 1:
    valor_final = valor_etiqueta * 0.85

if codigo_pagamento == 2:
    valor_final = valor_etiqueta * 0.9

if codigo_pagamento == 3:
    valor_final = valor_etiqueta

if codigo_pagamento == 4:
    valor_final = valor_etiqueta * 1.1

print("Valor final a pagar:",valor_final)