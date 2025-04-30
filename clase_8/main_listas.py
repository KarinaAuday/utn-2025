from funciones_listas import *


lista_interseccion = interseccion([1, 2, 3, 4,6], [3, 4, 5, 6])  # Encuentra la intersección entre dos listas
print ("Lista Interseccion")
for i in range(len(lista_interseccion)):
    print(f"Elemento {i}: {lista_interseccion[i]}")  # Imprime el elemento en la posición i
    
    
lista = ["pepe", "maria", "juan", "luis" , "pepe"]  # Inicializa una lista con valores
encontro = buscar_texto(lista, "Kari" )  # Busca el texto en la lista
print(encontro)  # Imprime si se encontró el texto
#lista = reemplazar_nombre(lista, "pepe", "Kari")  # Reemplaza el nombre en la lista
cant_remplazos = remplazar_nombres(lista, "pepe", "Kari")  # Reemplaza el nombre en la lista
print(f"Se reemplazaron {cant_remplazos} nombres")  # Imprime la cantidad de nombres reemplazados
for i in range(len(lista)):
    print(f"Elemento {i}: {lista[i]}")  # Imprime el elemento en la posición i
    

#mi_lista = [40, 50, 60, 150, 80]  # Inicializa una lista con valores
#promedio = calcular_promedio(mi_lista)  # Calcula el promedio de la lista
#print(f"El promedio de la lista es: {promedio}")  # Imprime el promedio de la lista
#pos_maxima = calcular_maximo(mi_lista)  # Busca el máximo de la lista
#print(f"el máximo de la lista es: {mi_lista[pos_maxima]}")  # Imprime el máximo de la lista


#lista = inicializar_lista_con_ingreso(5)  # Inicializa una lista vacía de tamaño 10
#for i in range(len(lista)):
 #   print(f"Elemento {i}: {lista[i]}")  # Imprime el elemento en la posición i
#lista = [0] * 5  # Inicializa una lista vacía de tamaño 10
#print (f"Lista original" ,lista)  # Imprime la lista completa
#mi_lista = ingresar_datos_lista (lista)
#cant_pares = contar_pares_lista(mi_lista)
#print(f"La cantidad de números pares en la lista es: {cant_pares}")  # Imprime la cantidad de números pares en la lista

