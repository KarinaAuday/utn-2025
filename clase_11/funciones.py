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

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial:any) -> list:
    """
    Esta función inicializa una matriz de tamaño filas x columnas con un valor dado.
    """
    matrix = []
    for i in range (cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matrix += [fila]
    return matrix


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

def cargar_recaudacion (recaudaciones, legajos) -> None:
    #valido el legajo
    legajo = int(input("Ingrese el legajo del chofer: "))
    existe_legajo = buscar_numero(legajos, legajo)
    while not existe_legajo:
        print("El legajo ingresado no es válido.")
        legajo = int(input("Ingrese el legajo del chofer: "))
        existe_legajo = buscar_numero(legajos, legajo)
    #valido linea
    linea = validar_int_en_rango("Ingrese la línea (1-3): ", 1, 3)
    #valido coche
    coche = validar_int_en_rango("Ingrese el coche (1-5): ", 1, 5)
    #valido recaudacion
    recaudacion = validar_int_en_rango("Ingrese la recaudación: ", 0)
    
    recaudaciones[linea - 1][coche - 1] += recaudacion
    print("Recaudación cargada con éxito.")
    
def mostrar_reacudacion_por_linea (recaudaciones , cant_lineas , cant_coches):
    print("\n--- Recaudación por línea ---")
    for i in range (cant_lineas):
        recaudacion_linea = 0
        for j in range (cant_coches):
            recaudacion_linea += recaudaciones[i][j]
        print (f"Línea {i + 1}: ${recaudacion_linea}")
    print()    
        
def mostrar_recaudacion_por_coche (recaudaciones , nro_coche , cant_lineas):
    print("\n--- Recaudación por coche ---")
    total_coche = 0
    for i in range (cant_lineas):
        total_coche += recaudaciones[i][nro_coche - 1]
    print (f"Coche {nro_coche}: ${total_coche}")    
       

def mostrar_recaudacion_total (recaudaciones):
    print("\n--- Recaudación total ---")
    total = 0
    for i in range (len(recaudaciones)):
        for j in range (len(recaudaciones[i])):
            total += recaudaciones[i][j]
    print (f"Total: ${total}")
    