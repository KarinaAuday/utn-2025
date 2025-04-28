# Este módulo contiene funciones para validar entradas de usuario.
# -*- coding: utf-8 -*-

""" valida texto y numeros en rango """


def validar_texto(mensaje):
    valor = input(mensaje)
    while valor.strip() == "":
        # Si el texto está vacío, solicita nuevamente
        if valor.strip() == "":
            print("El texto no puede estar vacío. Intenta de nuevo.")
            valor = input(mensaje)
    # Si el texto no está vacío, lo devuelve
    return valor


def validar_entero(mensaje, min , max = None)->int:  # minimo es obligatorio pero no se usa
    numero_entero = int(input(mensaje))    
    if max is not None:
        es_valido = numero_entero >= min and numero_entero <= max
    else:
        es_valido = numero_entero >= min
    while not es_valido:
        # Si el número no está en el rango, solicita nuevamente
        print("Debes ingresar un número entero válido entre", min, "y", max if max is not None else "infinito")
        numero_entero = int(input(mensaje))
        if max is not None:
           es_valido = numero_entero >= min and numero_entero <= max
        else:
           es_valido = numero_entero >= min
    return numero_entero

def validar_decimal(mensaje, min , max = None)->float:  # minimo es obligatorio pero no se usa
    numero_decimal = float(input(mensaje))    
    if max is not None:
        es_valido = numero_decimal >= min and numero_decimal <= max
    else:
        es_valido = numero_decimal >= min
    while not es_valido:
        # Si el número no está en el rango, solicita nuevamente
        print("Debes ingresar un número entero válido entre", min, "y", max if max is not None else "infinito")
        numero_decimal = float(input(mensaje))
        if max is not None:
           es_valido = numero_decimal >= min and numero_decimal <= max
        else:
           es_valido = numero_decimal >= min
    return numero_decimal

def validar_longitud (mensaje, cant):
    """Valida la longitud de un texto."""
    texto = input(mensaje)
    texto_valido = len(texto) == cant 
    while not texto_valido:
        # Si la longitud no es válida, solicita nuevamente
        texto = input(mensaje)
        texto_valido = len(texto) == cant 
    return texto

def validar_email(mensaje):
    """Valida un email."""
    email = input(mensaje)
    while "@" not in email or "." not in email:
        # Si el email no es válido, solicita nuevamente
        print("El email ingresado no es válido. Intenta de nuevo.")
        email = input(mensaje)
    return email

def legajo_valido(mensaje, largo, caracter, posicion) -> bool:
    """Valida un caracter."""
    legajo = input(mensaje)
    valido = True
    
    if len(legajo) != largo or legajo[posicion] == caracter:
        # Si el caracter no es válido, solicita nuevamente
        print("El caracter ingresado no es válido")
        valido = False
    
    return valido
