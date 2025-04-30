from funciones_listas import *  # Importa todas las funciones del módulo funciones_listas
lista_nombres = ["pepe", "maria", "juan", "luis" , "Ana"]  # Inicializa una lista con valores
lista_edades = [20, 30, 40, 50, 60]  # Inicializa una lista con valores
for i in range(len(lista_nombres)):
    print(f"Nombre: {lista_nombres[i]}, su edad es: {lista_edades[i]}") 
    
    # Imprime el elemento en la posición i
    
posicion_busqueda = buscar_texto_pos(lista_nombres, "ana")  # Busca el texto en la lista    
if posicion_busqueda != -1:
    print(f"La edad de Ana es : {lista_edades[posicion_busqueda]}")  # Imprime si se encontró el texto