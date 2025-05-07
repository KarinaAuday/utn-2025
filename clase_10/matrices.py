def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial:any) -> list:
    """
    Esta función inicializa una matriz de tamaño filas x columnas con un valor dado.
    """
    matrix = []
    for i in range (cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matrix += [fila]
    return matrix

def mostrar_matriz (matriz: list) -> None:
    """
    Esta función muestra una matriz en la consola.
    """
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            print (matriz[i][j], end = " ")
        print ()
def cargar_matriz_secuencialmente (matriz: list):
    """
    Esta función carga una matriz de forma secuencial.
    """
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            matriz[i][j] = int(input(f"Ingrese el valor para la posición ({i}, {j}): "))
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

def cargar_matriz_aleatoriamente (matriz: list , cant_filas , cant_columnas):
    seguir = "S"
    while seguir == "S":
        fila = validar_int_en_rango("Ingrese la fila: ", 1, cant_filas)
        columna = validar_int_en_rango("Ingrese la columna: ", 1, cant_columnas)
        valor = int(input("Ingrese el valor: "))
        matriz[fila - 1][columna - 1] = valor
        seguir = input("¿Desea continuar? (S/N): ").upper()

def mostrar_pos_valor_encontrado (matriz : list , valor : int ):
    """
    Esta función muestra la posición de un valor en una matriz.
    """
    filas = len(matriz)
    columnas = len (matriz[0])
    for i in range (filas):
        for j in range (columnas):
            print(f"valor actual para ({i}, {j}) es {matriz[i][j]}") 
            if matriz[i][j] == valor:
               
               print(f"El valor {valor} se encuentra en la posición ({i}, {j})")
               
               

def buscar_valor_matriz (matriz: list, filas , columnas, valor: int) -> bool:
    """
    Esta función busca un valor en una matriz y devuelve True o False.
    """
    i = 0
    encontrado = False
    while i < filas and not encontrado: 
        j = 0
        while j < columnas and not encontrado: 
            if matriz[i][j] == valor:  
                encontrado = True  
            j += 1
        i += 1
    return encontrado

CANT_FILAS = 2
CANT_COLUMNAS = 3
mi_matriz = inicializar_matriz(CANT_FILAS, CANT_COLUMNAS, 0)
mostrar_matriz(mi_matriz)

#cargar_matriz_secuencialmente(mi_matriz)
cargar_matriz_aleatoriamente(mi_matriz , CANT_FILAS , CANT_COLUMNAS)
print("Cantidad de filas " , len (mi_matriz))
print("Cantidad de columnas " , len (mi_matriz[0]))
print("Matriz cargada:")
mostrar_matriz(mi_matriz)
mostrar_pos_valor_encontrado (mi_matriz , 5)
encuentra_valor = buscar_valor_matriz(mi_matriz, len(mi_matriz), len(mi_matriz[0]), 5)
if encuentra_valor:
    print("El valor se encuentra en la matriz.")

