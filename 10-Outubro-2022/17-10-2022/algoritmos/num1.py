def decrescendo(x):
    print(x)
    if x == 1:
        return x
    else:
        return decrescendo(x-1)

decrescendo(10)