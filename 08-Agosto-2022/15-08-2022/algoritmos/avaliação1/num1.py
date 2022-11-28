alturaDegrau = float(input("Altura do degrau (em metros): "))
alturaDestino = float(input("Altura a alcançar (em metros): "))

numeroDegraus = alturaDestino // alturaDegrau

if alturaDestino % alturaDegrau != 0:
    numeroDegraus += 1

print(f"Precisa de {numeroDegraus} degraus")