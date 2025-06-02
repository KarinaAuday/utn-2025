import copy

#Funcion de busqueda
""" valida texto """    
def validar_texto_vacio(mensaje):
    texto = input(mensaje)
    texto = texto.strip()  # Elimina espacios en blanco al principio y al final
    while texto == "":
        # Si el texto está vacío, solicita nuevamente
        print("El texto no puede estar vacío. Intenta de nuevo.")
        texto = input(mensaje)
        texto = texto.strip()
    return texto 

def validar_int_en_rango (mensaje : str , min : int , max : int = None)->int:
    numero = int(input(mensaje))
    if max is None:
        es_valido = numero >= min
    else:
        es_valido = numero >= min and numero <= max
    while not es_valido:
        # Si el número no está en el rango, solicita nuevamente
        print("Debes ingresar un número entero válido entre", min, "y", max if max is not None else "infinito")
        numero = int(input(mensaje))
        if max is None:
            es_valido = numero >= min
        else:
            es_valido = numero >= min and numero <= max
    return numero


def buscar_legajo( lista ,legajo):
    i=0
    indice_encontrado = -1
    encontrado = False
    while i < len(lista) and encontrado == False:
        if lista[i] == legajo:
            indice_encontrado = i
            encontrado = True
        i += 1
    return indice_encontrado


def buscar_nombre( lista ,nombre):
    i=0
    indice_encontrado = -1
    encontrado = False
    while i < len(lista) and encontrado == False:
        if lista[i].upper() == nombre.upper():
            indice_encontrado = i
            encontrado = True 
        i += 1
    return indice_encontrado

def alta_estudiante (nombres , legajos , edades):
    nombre = validar_texto_vacio("Ingrese el nombre del estudiante: ")
    legajo = validar_int_en_rango("Ingrese el legajo del estudiante: ", 1000, 9999)
    edad = validar_int_en_rango("Ingrese la edad del estudiante: ", 1, 120)
    indice_alumno = buscar_legajo(legajos, legajo)
    if indice_alumno == -1:
        nombres.append(nombre)
        legajos.append(legajo)
        edades.append(edad)
        print("Estudiante agregado correctamente.")
    else:
        print("El legajo ya existe. No se puede agregar el estudiante.")    
        
def baja_estudiante(nombres, legajos, edades):
    legajo = validar_int_en_rango("Ingrese el legajo del estudiante a eliminar: ", 1000, 9999)
    indice_alumno = buscar_legajo(legajos, legajo)
    if indice_alumno != -1:
        nombres.pop(indice_alumno)
        legajos.pop(indice_alumno)
        edades.pop(indice_alumno)
        print("Estudiante eliminado correctamente.")
    else:
        print("El legajo no existe. No se puede eliminar el estudiante.")
        
def modificar_estudiante(nombres, legajos, edades):
    legajo = validar_int_en_rango("Ingrese el legajo del estudiante a modificar: ", 1000, 9999)
    indice_alumno = buscar_legajo(legajos, legajo)
    if indice_alumno != -1:
        print("Datos actuales del estudiante:")
        print(f"Nombre: {nombres[indice_alumno]}, Legajo: {legajos[indice_alumno]}, Edad: {edades[indice_alumno]}")
        opcion = int(input("Seleccione qué dato desea modificar:\n1. Nombre\n2. Edad\nIngrese su opción: "))
        if opcion == 1:
            nuevo_nombre = validar_texto_vacio("Ingrese el nuevo nombre del estudiante: ")
            nombres[indice_alumno] = nuevo_nombre
            print("Nombre modificado correctamente.")
        elif opcion == 2:
            nueva_edad = validar_int_en_rango("Ingrese la nueva edad del estudiante: ", 1, 120)
            edades[indice_alumno] = nueva_edad
            print("Edad modificada correctamente.")
        else:
            print("Opción no válida.")
        nombre = validar_texto_vacio("Ingrese el nuevo nombre del estudiante: ") 
    else:
        print("El legajo no existe. No se puede modificar el estudiante.")  
        
def listar_estudiantes(nombres, legajos, edades):  
    nombres_ordenados = nombres.copy()
    nombres_ordenados.sort()  
    #Listar comun
    for nombre, legajo, edad in zip(nombres, legajos, edades):
        print(f"Nombre: {nombre}, Legajo: {legajo}, Edad: {edad}")
    
    for index , nombre in enumerate(nombres_ordenados):
        print(f"{index + 1}. Nombre: {nombre}")
              
              
def buscar_estudiante_por_nombre(nombres, legajos, edades):
    nombre_buscado = validar_texto_vacio("Ingrese el nombre del estudiante a buscar: ")
    indice_alumno = buscar_nombre(nombres, nombre_buscado)
    if indice_alumno != -1:
        print(f"Estudiante encontrado: Nombre: {nombres[indice_alumno]}, Legajo: {legajos[indice_alumno]}, Edad: {edades[indice_alumno]}")
    else:
        print("El estudiante no fue encontrado.")
        
def clonar_base_datos(nombres, legajos, edades):
    # Shallow copy
    nombres_shallow = nombres.copy()
    legajos_shallow = legajos.copy()
    edades_shallow = edades.copy()
    
    # Deep copy
   
    nombres_deep = copy.deepcopy(nombres)
    legajos_deep = copy.deepcopy(legajos)
    edades_deep = copy.deepcopy(edades)
    
    print("Clonación realizada (shallow copy y deep copy).")
    print("Shallow Copy:")
    print(f"Nombres: {nombres_shallow}, Legajos: {legajos_shallow}, Edades: {edades_shallow}")
    print("Deep Copy:")
    print(f"Nombres: {nombres_deep}, Legajos: {legajos_deep}, Edades: {edades_deep}")
    
    
def vaciar_base_datos(nombres, legajos, edades):
    nombres.clear()
    legajos.clear()
    edades.clear()
    print("Base de datos vaciada correctamente.")
    return nombres, legajos, edades        