from funciones import *
nombres=["Juan", "Ana", "Pedro", "Maria"]
legajos=[1001, 1002, 1003, 1004]
edades=[20, 22, 21, 23]




def menu():
    opcion = 0
    
    while opcion !=8:

        print("\n--- Menú de Gestión de Estudiantes ---")
        print("Seleccione una opción:")
        print("1. Alta de estudiante (cargar nuevo estudiante)")
        print("2. Baja de estudiante (eliminar por número de legajo)")
        print("3. Modificar datos de estudiante (nombre o edad, buscar por legajo)")
        print("4. Listar todos los estudiantes (ordenados por nombre)")
        print("5. Buscar estudiante por nombre (mostrar legajo y edad)")
        print("6. Clonar base de datos (shallow copy y deep copy)")
        print("7. Vaciar base de datos (clear)")
        print("8. Salir") 
        opcion = int(input("Seleccione una opción: "))
        match opcion:
            case 1:
                alta_estudiante(nombres, legajos, edades)
            case 2:
                baja_estudiante(nombres, legajos, edades)
            case 3:
                modificar_estudiante(nombres, legajos, edades)
            case 4:
                listar_estudiantes(nombres, legajos, edades)
            case 5:
                buscar_estudiante_por_nombre(nombres, legajos, edades)
            case 6:
                clonar_base_datos(nombres, legajos, edades)
            case 7:
                vaciar_base_datos(nombres, legajos, edades)
            case 8:
                print("Saliendo del programa...")
            case _:
                print("Opción no válida. Intente nuevamente.")
menu()