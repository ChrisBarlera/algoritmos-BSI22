paisA = 80000
paisB = 200000

qtdAnos = 0
while paisA < paisB:
    paisA *= 1.03
    paisB *= 1.015
    qtdAnos += 1
    
print(f"Após {qtdAnos} anos, o país A superou o B em população")