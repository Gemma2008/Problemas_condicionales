def multiplo_tres(num):
    if (num%3 == 0):
        return(print("El numero es multiplo de 3"))
    else:
        return(print("El numero  no es multiplo de tres"))
    
num = int(input("Dime un numero: "))
multiplo_tres(num)
