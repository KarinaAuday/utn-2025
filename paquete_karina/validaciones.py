"""  Este módulo contiene funciones para validar datos de entrada en un sistema de gestión de inventario.
Las funciones incluyen validaciones para texto, números enteros y decimales, longitud de texto y correos electrónicos.
"""

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


def texto_valido(texto):
    es_valido = False
    texto = texto.strip()  # Elimina espacios en blanco al principio y al final
    if texto != "":
         es_valido = True
    return es_valido
 
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
        

def validar_acceso(usuario_correcto, clave_correcta, intentos_max): 
    intentos = 0    
    ingreso_correcto = False
    while intentos < intentos_max and not ingreso_correcto: 
         usuario = input("Ingrese su usuario: ") 
         clave = input("Ingrese la clave: ")
         ingreso_correcto = (usuario == usuario_correcto and clave == clave_correcta)
         intentos += 1
         
    if ingreso_correcto:    
       mensaje = "Acceso concedido."
    else:
       mensaje = "Acceso denegado. Se han agotado los intentos."  
             
    return mensaje   


def validar_legajo(mensaje):
    numero_legajo = int(input(mensaje))
    legajo_correcto= numero_legajo >= 1000 and numero_legajo <= 9999
    while not legajo_correcto:
          print("El número de legajo no puede ser menor a 4 digitos ni debe contener 0  a la izquierda.")
          numero_legajo = int(input(mensaje))
          legajo_correcto= numero_legajo >= 1000 and numero_legajo <= 9999
    return numero_legajo     