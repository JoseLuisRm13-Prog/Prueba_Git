def Sumamos(Numero_1, Numero_2):
        suma = Numero_1+Numero_2
        return suma

def multiplicamos(Numero_1, Numero_2):
        multi = Numero_1*Numero_2
        return multi

def Dividir(Numero_1, Numero_2):
        Div = Numero_1/Numero_2
        return Div

def Restar(Numero_1, Numero_2):
        Resta = Numero_1-Numero_2
        return Resta

def contador(Numero_1,Numero_2):
        Mi_array = []
        cont = 0
        for Numero_1 in range(Numero_2):
                Mi_array.append(Numero_1+1)
        return Mi_array

def Multi_Lista(lista):
        resultado =  lista[0]*lista[1]*lista[2]*lista[3]*lista[4]
        return  resultado

def Agregar_productos(producto, precio):
        carrito = {producto:precio}
        return carrito
        