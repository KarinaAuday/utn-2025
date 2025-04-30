def mostrar_lista_for(lista):
    """
    Esta función imprime los elementos de una lista.
    """
    for i in range(len(lista)):
        print(f"Elemento {i}: {lista[i]}")  # Imprime el elemento en la posición i
        
def mostrar_lista_while(lista):
    """
    Esta función imprime los elementos de una lista.
    """
    i = 0
    while i < len(lista):
        print(f"Elemento {i}: {lista[i]}")  # Imprime el elemento en la posición i
        i += 1        
        
def sumar_lista (lista):
    """
    Esta función suma los elementos de una lista.
    """
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]  # Suma el elemento en la posición i
    return suma

def contar_pares_lista (lista):
    sumar_pares = 0
    i = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:  # Verifica si el elemento es par
            sumar_pares += 1  # Suma el elemento en la posición i
    return sumar_pares       

def ingresar_datos_lista (lista):
    """
    Esta función ingresa datos en una lista.
    """
    # Inicializa una lista vacía
    for i in range(len(lista)):
        valor = int(input(f"Ingrese el valor para la posición {i}: "))  # Solicita el valor al usuario
        lista[i] = valor  # Asigna el valor a la posición i de la lista
    return lista


def inicializar_lista (cantidad , valor)-> list:
    """""
    Esta función inicializa una lista con un valor específico.
    """
    lista = [valor] * cantidad
    # Inicializa una lista vacía
    return lista

def inicializar_lista_con_ingreso (cantidad)-> list:
    lista = [0] * cantidad  # Inicializa una lista vacía de tamaño 10 
    for i in range(0, cantidad):
        valor = int(input(f"Ingrese el valor para la posición {i}: "))  # Solicita el valor al usuario
        lista[i] = valor  # Asigna el valor a la posición i de la lista
    return lista

def calcular_promedio (lista):
    """
    Esta función calcula el promedio de los elementos de una lista.
    """
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]  # Suma el elemento en la posición i
    promedio = suma / len(lista)  # Calcula el promedio
    return promedio


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
#--------------------------------- BUSQUEDAS EN LISTAS ------------------------------------------
    """
    EJEMPLOS DE MALAS y BUENAS PRACTICAS PARA BUSCAR EN UNA LSITA"
    
    """
#LO QUE NOOOOOOOOOO HAY QUE HACER  ---> FOR CON BREAK
def buscar_texto_mal1 (lista , texto)->bool: 
    encontrado = False
    for i in range(len(lista)):
        if lista[i].upper() == texto.upper(): 
           encontrado = True  
           break  
    return encontrado  
#LO QUE NOOOOOOOOOO HAY QUE HACER  ---> EARLY RETURN
def buscar_texto_mal2 (lista , texto)->bool: 
    for i in range(len(lista)):
        if lista[i].upper() == texto.upper(): 
           return True   
    return False  

#LO QUE NOOOOOOOOOO HAY QUE HACER  ---> FOR QUE NO TERMINA CUANDO ENCUENTRA
def buscar_texto_mal3 (lista , texto)->bool: 
    encontrado = False
    for i in range(len(lista)):
        if lista[i].upper() == texto.upper():  # Verifica si el elemento es igual al texto buscado
           encontrado = True  
    return encontrado  # Retorna True si se encontró el texto, False en caso contrario   

#LO QUE SIIIIIIIIIIIII  HACEMOS   -> WHILE MIENTRAS NO ENCUENTRA SIGUE HASTA EL MAXIMO DE LA LISTA
def buscar_texto (lista , texto)->bool:
    """
    Esta función busca un texto en una lista.
    """
    encontrado = False
    i = 0
    while i < len(lista) and not encontrado:  # Repite mientras no se haya encontrado el texto
        if lista[i].upper() == texto.upper():  # Verifica si el elemento es igual al texto buscado
            encontrado = True  # Cambia la variable a True si se encuentra el texto
        i += 1  # Incrementa el índice para pasar al siguiente elemento
    return encontrado  # Retorna True si se encontró el texto, False en caso contrario

def buscar_texto_pos (lista , texto)->int:
    """
    Esta función busca un texto en una lista y devuelve una posicion.
    """
    encontrado = False
    i = 0
    pos_encontrado = -1
    while i < len(lista) and not encontrado: 
        if lista[i].upper() == texto.upper():
            pos_encontrado = i
            encontrado = True  
        i += 1  
    return pos_encontrado  #Devuelve la posicion donde encontro el texto

#Esta funcion recibe un nombre y remplaza con otro en el lugar que encontro ese nombre  
def reemplazar_nombre (lista , nombre_a_reemplazar , nuevo_nombre)->list:
    """
    Esta función reemplaza un nombre en una lista por otro.
    """
    pos = buscar_texto_pos (lista , nombre_a_reemplazar)
    if pos != -1:
        lista[pos] = nuevo_nombre
    return lista  # Retorna la lista con el nombre reemplazado

def remplazar_nombres (lista , nombre_a_reemplazar , nuevo_nombre)->int:
    """
    Esta función reemplaza un nombre en una lista por otro y devuelve cuantos remplazo se hicieron.
    """
    cont = 0
    for i in range(len(lista)):
        if lista[i].upper() == nombre_a_reemplazar.upper():
            cont += 1
            lista[i] = nuevo_nombre
    return cont  # Retorna la lista con el nombre reemplazado

def interseccion (lista1 , lista2)->list:
    """
    Esta función encuentra la intersección entre dos listas.
    """
    lista_interseccion = []  #Uso append que agrega una posicion
    for i in range(len(lista1)):
        numero_buscar = lista1[i]  # Asigna el elemento de la lista1 a buscar
        pos = buscar_numero(lista2 , numero_buscar)  # Busca el número en la segunda lista
        if pos != -1:
            lista_interseccion.append(lista1[i])
       
    return lista_interseccion  # Retorna la lista de intersección

def buscar_numero ( lista , numero)->int:
    """
    Esta función busca un número en una lista y devuelve la posición donde se encontró.
    """
    encontrado = False
    i = 0
    pos_encontrado = -1
    while i < len(lista) and not encontrado: 
        if lista[i] == numero:
            pos_encontrado = i
            encontrado = True  
        i += 1  
    return pos_encontrado  #Devuelve la posicion donde encontro el texto