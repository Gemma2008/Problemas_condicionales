def rango_edad(edad):
    if (edad < 18):
        return(print("Eres menor de edad"))
    elif(edad < 65):
        return(print("Eres adulto"))
    else:
        return(print("Eres adulto mayor"))
    
edad = int(input("Dime tu edad: "))
rango_edad(edad)
