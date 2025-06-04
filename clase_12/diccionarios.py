from modulo_normalizacion import *

def menu():
    opcion = 0
    while opcion != 10 and opcion != 1:
        print("***** Bienvenido al menú de la playlist de Lady Gaga *****")
        print("1. Salir")
        print("2. Mostrar lista de temas")
        print("3. Ordenar Temas")
        print("4. Promedio de vistas")
        print("5. Máxima reproducción")
        print("6. Mínima reproducción")
        print("7. Búsqueda por código")
        print("8. Listar por colaborador")
        print("9. Listar por Mes de Lanzamiento")
        print("10. Salir")

        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 2:
                mostrar_lista_temas(canciones)
            case 3:
                ordenar(canciones)
                print("Canciones ordenadas!")
            #case 4:
            #case 5:
            #case 6:
            #case 7:
            #case 8:
            #case 9:
            
            case 10 | 1:
                print("Gracias por usar el programa. ¡Hasta luego!")

def mostrar_lista_temas(canciones):
    print(f"{'Título':<55} {'Duración (s)':>8}")
    print("-" * 68)
    for cancion in canciones:
        print(f"{cancion['Titulo']:<55} {cancion['Duracion']:>8}")

def ordenar(canciones):
    for cancion in range(len(canciones) - 1):
        for j in range(len(canciones) - 1 - cancion):
            if canciones[j]["Duracion"] < canciones[j + 1]["Duracion"]:
                canciones[j], canciones[j + 1] = canciones[j + 1], canciones[j]
    

canciones = normalizacion()
menu()