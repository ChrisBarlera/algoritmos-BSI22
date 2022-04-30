#Declare as seguintes variáveis: nome do funcionario, anoNascimento, numero de filhos, rg, salario, ativo. Atribua valores às respectivas variáveis. A variável ativo deverá receber um valor lógico. Mostre os dados conforme exemplo abaixo:

# O funcionário <<nome>> com rg <<rg>> possui <<>> anos de vida. O salario do funcionario <<nome>> é de R$ << salario>> e possui << >> filhos. Situação ativo:<<ativo>>

nome = input("Nome: ")
anoNascimento = int(input("Ano de nascimento: "))
numFilhos = int(input("Número de filhos: "))
numRG = int(input("Número de RG: "))
salario = float(input("Salário: "))
status = bool(int(input("Situação de atividade (0 para inativo, 1 para ativo): ")))

idade = 2022 - anoNascimento

print("\nO funcionário",nome,"com RG",numRG,"possui",idade,"anos de vida. O salário do funcionário",nome,"é de",salario,"e possui",numFilhos,"filhos. Situação de atividade:",status)