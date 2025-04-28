


def crear_lista(cantidad):
    lista =  [None] * cantidad# Inicializa una lista vacía
    return lista

def modificar_lista (indice , valor , lista):
    if indice >= 0 and indice < len(lista):
       lista[indice] = valor # Modifica el valor en la posición indicada
    else:
        print("Índice fuera de rango")   
    return lista
 
# Ejemplo:
#array = crear_array(5)
#array = [1, 2, 3, 4, 5]  # Asignar valores a la lista
#print(array)  

#lista_numeros = [101, 25, -50, 88, 0]
#print  (id(lista_numeros))  # Imprime la lista completa


lista = crear_lista(10)  #Crea con valores None
print (f"Lista original" ,lista)  # Imprime la lista completa
print (f"Id lista original", id(lista))  # Imprime la lista completa
lista_modificada = modificar_lista(0, 10, lista) # Modifica el valor en la posición 0 de la lista que le póne un 10
print (f"Lista modificada" ,lista_modificada)  # Imprime la lista completa
print (f"Id lista modificada", id(lista_modificada))  # Imprime la lista completa
print (f"Lista original" ,lista)  # Imprime la lista completa
print (f"Id lista original", id(lista))  # Imprime la lista completa
lista_modificada = modificar_lista(9, 200, lista) # Modifica el valor en la posición 0 de la lista que le póne un 10
ultimo_elemento = lista_modificada[(len(lista_modificada) - 1)] # Accede al último elemento de la lista
print (f"Último elemento de la lista modificada: {ultimo_elemento}")  # Imprime el último elemento de la lista modificada