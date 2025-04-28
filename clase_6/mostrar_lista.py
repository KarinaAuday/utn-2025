def mostrar_lista_for(lista):
    """
    Esta función imprime los elementos de una lista.
    """
    for i in range(len(lista)):
        print(f"Elemento {i}: {lista[i]}")  # Imprime el elemento en la posición i
        
def mostrar_lista_while(lista):
    """
    Esta función imprime los elementos de una lista.
    """
    i = 0
    while i < len(lista):
        print(f"Elemento {i}: {lista[i]}")  # Imprime el elemento en la posición i
        i += 1        
        
def sumar_lista (lista):
    """
    Esta función suma los elementos de una lista.
    """
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]  # Suma el elemento en la posición i
    return suma

def contar_pares_lista (lista):
    sumar_pares = 0
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:  # Verifica si el elemento es par
            sumar_pares += 1  # Suma el elemento en la posición i
        i += 1
    return sumar_pares       

def ingresar_datos_lista (lista):
    """
    Esta función ingresa datos en una lista.
    """
    # Inicializa una lista vacía
    for i in range(len(lista)):
        valor = int(input(f"Ingrese el valor para la posición {i}: "))  # Solicita el valor al usuario
        lista[i] = valor  # Asigna el valor a la posición i de la lista
    return lista


lista = [0] * 5  # Inicializa una lista vacía de tamaño 10
print (f"Lista original" ,lista)  # Imprime la lista completa
mi_lista = ingresar_datos_lista (lista)
cant_pares = contar_pares_lista(mi_lista)
print(f"La cantidad de números pares en la lista es: {cant_pares}")  # Imprime la cantidad de números pares en la lista

