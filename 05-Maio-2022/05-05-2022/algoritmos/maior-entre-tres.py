num_A = int(input("Valor A: "))
num_B = int(input("Valor B: "))
num_C = int(input("Valor C: "))

if num_A > num_B and num_A > num_C:
    maior = num_A

if num_B > num_C and num_B > num_A:
    maior = num_B

if num_C > num_A and num_C > num_B:
    maior = num_C

print("O maior numéro é:",maior)