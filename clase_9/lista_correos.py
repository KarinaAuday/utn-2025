from validaciones_2 import *  
from funciones_arrays import *
# Se tienen dos listas paralelas: una representa los nombres de quienes 
# viven en los pisos de un edificio (10 pisos)
# y la otra representa la cantidad de correos que llegan a cada piso.
# El programa permite al usuario ingresar los pisos y la cantidad de correos recibidos
# en cada uno.
#El proceso se repite hasta que el usuario ingrese 0 como número de piso,
# lo que terminará el ingreso de datos.
#Las cantidades de correos se suman en una lista paralela correspondiente.

CANT_PISOS = 6
lista_pisos = ["Jaun", "Pedro", "Maria", "Ana", "Luis", "Carlos"]
lista_correos = [0] * CANT_PISOS  # Inicializa la lista de correos con ceros
piso = validar_int_en_rango("Ingrese el piso (1-6) donde quiere ingresar o 0 para terminar: ", 0, CANT_PISOS)
if piso != 0:
    cant_correo = validar_int_en_rango (f"Ingrese cuantas cartas le llegaron la piso {piso + 1} : ", 1 )
while piso != 0:
    lista_correos[piso - 1] += cant_correo  # Suma la cantidad de correos al piso correspondiente
    piso = validar_int_en_rango("Ingrese el piso (1-6) donde quiere ingresar o 0 para terminar: ", 0, CANT_PISOS)
    if piso != 0:
        cant_correo = validar_int_en_rango (f"Ingrese cuantas cartas le llegaron la piso {piso + 1} : ", 1 )
# Mostrar la lista de correos por piso  
for i in range(CANT_PISOS):
    if lista_correos[i] > 0:  # Verifica si hay correos en el piso
        # Si hay correos, lo muestra
        print(f"En el piso {i + 1} viven: {lista_pisos[i]} y le llegaron {lista_correos[i]} correos.")
    else:
        # Si no hay correos, muestra un mensaje indicando que está vacío
        print (f"En el piso {i + 1} no hay vecinos y no le llegaron correos.")