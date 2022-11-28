x = float(input("Valor X: "))
y = float(input("Valor Y: "))

if (x + y)*0.3 > 500:
    aux = x
    x = y
    y = aux
    print(f"valores atuais de x e y, respectivamente: {x,y}")
else:
    if x < y:
        print("menor valor:",x)
    else:
        print("menor valor:",y)