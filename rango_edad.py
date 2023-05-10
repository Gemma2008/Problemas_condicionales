def rango_edad(edad1):
    if edad1 < 18:
        return "eres menor de edad"
    elif edad1 >=65:
        return "eres adulto mayor"
    else:
        return "eres adulto"
    
edad1 = int(input("Dime tu edad "))
print(rango_edad(edad1))
