def union (lista1 , lista2):
    """
    Union de dos listas
    """
    longitud = len(lista1) + len(lista2)
    lista_union = [None] * longitud
    cont = 0
    for i in range(len(lista1)):
        lista_union[i] = lista1[i]
        cont += 1
    for i in range(len(lista2)):
        lista_union[cont] = lista2[i]  
        cont += 1
    return lista_union      

    
def diferencia (lista1 , lista2)->list:
    """
    Esta función encuentra la intersección entre dos listas.
    """
    longitud = len(lista1) + len(lista2)
    lista_diferencia = [None] * longitud
    cont = 0    
    for i in range(len(lista1)):
        texto_buscar = lista1[i]  # Asigna el elemento de la lista1 a buscar
        encontro = buscar_texto(lista2 , texto_buscar)  # Busca el número en la segunda lista
        if not encontro:  # Si no se encuentra el texto en la segunda lista
            lista_diferencia[cont] = texto_buscar # Agrega el texto a la lista de diferencia
            cont += 1
    for i in range(len(lista2)):
        texto_buscar = lista2[i]  # Asigna el elemento de la lista1 a buscar
        encontro = buscar_texto(lista1 , texto_buscar)  # Busca el número en la segunda lista
        if not encontro:  # Si no se encuentra el texto en la segunda lista
            lista_diferencia[cont] = texto_buscar # Agrega el texto a la lista de diferencia
            cont += 1        
    return lista_diferencia  # Retorna la lista de diferencia

         
def buscar_texto (lista , texto)->bool:
    """
    Esta función busca un texto en una lista y devuelve True o False
    """
    encontrado = False
    i = 0
    while i < len(lista) and not encontrado:  # Repite mientras no se haya encontrado el texto
        if lista[i].upper() == texto.upper():  # Verifica si el elemento es igual al texto buscado
            encontrado = True  # Cambia la variable a True si se encuentra el texto
        i += 1  # Incrementa el índice para pasar al siguiente elemento
    return encontrado  # Retorna True si se encontró el texto, False en caso contrario 

def mostrar_lista_salteando_valor(lista , valor_no_mostrar = None):
    """
    Muestra los elementos de una lista
    """
    for i in range(len(lista)):
        if lista[i] != valor_no_mostrar:
            print(lista[i])
