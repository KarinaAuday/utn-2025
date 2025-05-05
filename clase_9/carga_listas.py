from validaciones_2 import *  
from funciones_arrays import *
#Cargar lista de numeros de forma seleccionada
#Cargar los nombres de los vecinos un edificio de 6 pisos , seleccionando en que piso quiere ingresar. y que ingrese FIN para terminar

CANT_PISOS = 6
lista_pisos = [None] * CANT_PISOS


nombre = validar_texto_vacio("Ingrese el nombre del vecino (o 'FIN' para terminar): ")
if nombre.upper() != "FIN":
    piso = validar_int_en_rango("Ingrese el piso (1-6) donde quiere ingresar: ", 1, CANT_PISOS)
while nombre.upper() != "FIN":
    lista_pisos[piso - 1] = nombre  # Almacena el nombre en la posición correspondiente al piso
    nombre = validar_texto_vacio("Ingrese el nombre del vecino (o 'FIN' para terminar): ")
    if nombre.upper() != "FIN":
        piso = validar_int_en_rango("Ingrese el piso (1-6) donde quiere ingresar: ", 1, CANT_PISOS)   
     
   
for i in range(CANT_PISOS):
    if lista_pisos[i] is not None:  # Verifica si hay un nombre en la posición del piso
        # Si hay un nombre, lo muestra
        print(f"En el piso {i + 1} vive: {lista_pisos[i]}")
    else:        
        # Si no hay un nombre, muestra un mensaje indicando que está vacío
        print (f"En el piso {i + 1} no hay vecinos.")
        
        