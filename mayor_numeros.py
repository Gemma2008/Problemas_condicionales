def mayor(num1,num2):
    if (num1 > num2):
        return (print("El mayor es: ", num1))
    elif (num1 == num2):
        return(print("Son iguales"))
    else:
        return(print("El mayor es: ", num2))
    
num1 = int(input("Dime primer numero: "))
num2 = int(input("Dime el segundo numero: "))
mayor(num1,num2)
