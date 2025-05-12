from funciones import *

CANT_LINEAS = 3
CANT_COCHE = 5
CANT_CHOFERES = 15

def mostrar_recaudacion (recaudaciones):
    print("\n--- Recaudación por coche y línea ---")
    for i in range(CANT_LINEAS):
        for j in range(CANT_COCHE):
            print(f"Línea {i + 1}, Coche {j + 1}: ${recaudaciones[i][j]}")
    print()



def menu ():
    salir = False
    while not salir:
        print("\n--- MENÚ ---")
        print("1. Cargar recaudación")
        #Muestra la recaudación por coche y línea
        print("2. Mostrar recaudación de cada coche y línea")
        #Muestra la recaudación total por cada línea
        print("3. Mostrar recaudación total por cada línea")
        #Muestra la recaudación total para un coche seleccionado
        print("4. Mostrar recaudación para un coche seleccionado")
        #Muestra la recaudación total
        print("5. Mostrar recaudación total")
        #Muestra la recaudación total para cada coche
        print ("6. Mostrar recaudación  total para cada  coche")
        #Muestra la recaudación total para una línea seleccionada
        print("7. Mostrar recaudación total para una línea seleccionada")
        print("8. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            cargar_recaudacion(recaudaciones , legajos)
        if opcion == 2:
            mostrar_recaudacion(recaudaciones)    
            input("Presione Enter para continuar...")
        if opcion == 3:
           mostrar_reacudacion_por_linea(recaudaciones, CANT_LINEAS, CANT_COCHE)   
           input("Presione Enter para continuar...")
        if opcion == 4:
            nro_coche = validar_int_en_rango("Ingrese el número de coche (1-5): ", 1, 5)
            mostrar_recaudacion_por_coche(recaudaciones , nro_coche , CANT_LINEAS)   
            input("Presione Enter para continuar...") 
        if opcion == 5:
            mostrar_recaudacion_total (recaudaciones)
            input("Presione Enter para continuar...")   
        if opcion == 6:            
            input("Presione Enter para continuar...")
        if opcion == 7:           
            input("Presione Enter para continuar...")
        if opcion == 8:
            print("Saliendo del programa...")
            salir = True      
                  
#------------------------main----------------------------------------------------------
legajos = [1001 , 1002 , 1003 , 1004 , 1005 , 1006 , 1007 , 1008 , 1009 , 1010 , 1011 , 1012 , 1013 , 1014 , 1015]
recaudaciones = [
    [1, 1, 101, 41, 1],
    [2, 0, 5454, 50, 5],
    [3, 0, 666, 4, 5]
]
#recaudaciones = inicializar_matriz(CANT_LINEAS, CANT_COCHE, 0)
menu()