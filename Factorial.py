Numero = int(input("Ingrese Numero: "))

def Factorial(Number):
    Numero_salida = 0
    contador = 1
    Numero_actual = 1
    while (contador<=Number):
        Numero_salida = contador*Numero_actual
        contador+=1
        Numero_actual = Numero_salida
    return Numero_salida

print("El factorial es: ", Factorial(Numero))