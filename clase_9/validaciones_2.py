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


def validar_texto_vacio(mensaje):
    texto = input(mensaje)
    texto = texto.strip()  # Elimina espacios en blanco al principio y al final
    while texto == "":
        # Si el texto está vacío, solicita nuevamente
        print("El texto no puede estar vacío. Intenta de nuevo.")
        texto = input(mensaje)
        texto = texto.strip()
    return texto 