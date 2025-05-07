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


def ingresar_notas (lista , texto):
    """
    Esta función ingresa datos en una lista.
    """
    # Inicializa una lista vacía
    for i in range(len(lista)):
        valor = validar_int_en_rango(texto, 1, 10)  # Solicita el valor al usuario
        lista[i] = valor  # Asigna el valor a la posición i de la lista
    return lista

def ingresar_materias (lista , texto):
    """
    Esta función ingresa datos en una lista.
    """
    # Inicializa una lista vacía
    for i in range(len(lista)):
        valor = validar_texto_vacio(texto)  # Solicita el valor al usuario
        lista[i] = valor  # Asigna el valor a la posición i de la lista
    return lista


def inicializar_lista (cantidad , valor)-> list:
    """""
    Esta función inicializa una lista con un valor específico.
    """
    lista = [valor] * cantidad
    # Inicializa una lista vacía
    return lista
def calcular_maximo (lista)->int:
    """
    Esta función calcula el máximo de los elementos de una lista. retornar la posicion donde se encontro
    """
    maximo = float('-inf')  # Inicializa el máximo con el valor más pequeño posible
    pos = 0
    for i in range(len(lista)):
        if lista[i] > maximo:  # Verifica si el elemento es mayor que el máximo actual
            maximo = lista[i]  # Actualiza el máximo
            pos = i  # Actualiza la posición del máximo
    return pos  # Retorna la posición del máximo encontrado
def calcular_cant_notas (lista , valor)->int:
    """
    Esta función calcula la cantidad de notas mayores a un valor.
    """
    contador = 0
    for i in range(len(lista)):
        if lista[i] > valor:  # Verifica si el elemento es mayor que el máximo actual
            contador += 1  # Actualiza el máximo
    return contador  # Retorna la posición del máximo encontrado

def buscar_numero(lista , numero)->bool:
    """
    Esta función busca un texto en una lista.
    """
    encontrado = False
    i = 0
    while i < len(lista) and not encontrado:  
        if lista[i] == numero:  
            encontrado = True  
        i += 1  
    return encontrado 

def crear_arreglo(longitud: int, valor) -> list:
    lista = [valor] * longitud
    return lista

def mayores_lista_pos(lista: list) -> int:
    """
    Está función recorre una lista y puede devolver una lista con cada posición que contenga un valor igual al valor máximo 
    de la lista inicial
    """
    mayor = float('-inf')
    lista_mayores = crear_arreglo(len(lista), None)
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]

    contador = 0
    for i in range(len(lista)):
        if lista[i] == mayor:
            lista_mayores[contador] = i
            contador += 1

    return lista_mayores

#---------Programa Principal-------------------
CANT_ALUMNOS = 5
lista1 = inicializar_lista (CANT_ALUMNOS , "")
lista2 = inicializar_lista (CANT_ALUMNOS , 0)
lista_materias= ingresar_materias(lista1, "Ingrese el nombre de la materia: ")
lista_notas = ingresar_notas(lista2, "Ingrese la nota de la materia: ")
lista_notas_mayores = mayores_lista_pos(lista_notas)
for i in range(len(lista_notas_mayores)):
    if lista_notas_mayores[i] != None:
        print("La materia que tiene nota más alta es: ", lista_materias[lista_notas_mayores[i]])
cantidad_mayor_nota7 = calcular_cant_notas (lista_notas , 7)
print ("La cantidad de materias con nota mayor a 7 fueron " , cantidad_mayor_nota7)
encontro_nota = buscar_numero(lista_notas , 10)
if encontro_nota:
    print("Se encontró al menos una materia con nota 10.")
else:
    print("No se encontraron materias con la nota 10.")
    