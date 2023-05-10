def comparacion_palabras(palabra1,palabra2):
    if palabra1 == palabra2:
        return True
    else:
        return False
pab1 = (input("dime una palabra"))
pab2 = (input("dime otra palabra"))
print(comparacion_palabras(pab1,pab2))
