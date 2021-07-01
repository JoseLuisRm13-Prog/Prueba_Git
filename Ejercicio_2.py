
from Scripts.Funciones.funciones import *

Operacion = int(input("1 para sumar, 2 para multiplicar, 3 para dividir o otro para restar: "))
Numero_1 = int(input("Por favor digita el numero 1: "))
Numero_2 = int(input("Por favor digita un numero 2: "))

if Operacion == 1:
    resultado = Sumamos(Numero_1, Numero_2)
elif Operacion == 2:
    resultado = multiplicamos(Numero_1, Numero_2)
elif Operacion == 3:
    resultado = Dividir(Numero_1, Numero_2)
else:
    resultado = Restar(Numero_1, Numero_2)
    
print ("Resultado: ", resultado)

