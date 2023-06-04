def compara_palabras(pab1,pab2):
    if (pab1 == pab2):
        return(print("Son iguales"))
    else:
        return(print("Son diferentes"))
    
pab1 = str(input("Dime la primera palabra: "))
pab2 = str(input("Dime la segunda palabra: "))
compara_palabras(pab1,pab2)
