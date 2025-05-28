def ordenar_lista (lista , desc = False):
    """
    Esta función ordena una lista de números enteros de forma ascendente o descendente.
    """
    longitud = len(lista)
    for i in range (longitud):
        for j in range (longitud - 1):
            if desc:
                if lista[j] < lista[j + 1]:
                   aux = lista[j]
                   lista[j] = lista[j + 1]
                   lista[j + 1] = aux 
            else:
                if lista[j] > lista[j + 1]:
                   aux = lista[j]
                   lista[j] = lista[j + 1]
                   lista[j + 1] = aux   
                   

def ordenar_lista_mejorada (lista , desc = False):
    """
    Esta función ordena una lista de números enteros de forma ascendente o descendente.
    """
    longitud = len(lista)
    i = 0
    intercambiado = True
    while i < longitud and intercambiado:
        intercambiado = False
        for j in range (longitud - 1):
            if (desc and lista[j] < lista[j + 1]) or (not desc and lista[j] > lista[j + 1]):
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                intercambiado = True
        i += 1
                       
def mostrar_lista_salteando_valor(lista , valor_no_mostrar = None):
    """
    Muestra los elementos de una lista
    """
    for i in range(len(lista)):
        if lista[i] != valor_no_mostrar:
            print(lista[i])



def intercalar_vectores(v1, v2, descendente=False):
    n1 = len(v1)
    n2 = len(v2)
    resultado = [0] * (n1 + n2)

    i = 0
    j = 0
    k = 0
 
    while i < n1 and j < n2:
        if v1[i] < v2[j]:
            resultado[k] = v1[i]
            i += 1
        else:
            resultado[k] = v2[j]
            j += 1
        k += 1

    for m in range(i, n1):
        resultado[k] = v1[m]
        k += 1

    for m in range(j, n2):
        resultado[k] = v2[m]
        k += 1

    if descendente:
        ordenar_lista_mejorada(resultado, True)

    return resultado            
                            
lista = [45, 2, 9, 1, 5, 6]
ordenar_lista_mejorada(lista)
print("Lista ordenada")
mostrar_lista_salteando_valor(lista)
ordenar_lista_mejorada(lista , True)
print("Lista ordenada de forma descendente")
mostrar_lista_salteando_valor(lista)   
v1 = [3, 8, 55]
v2 = [22, 44, 111]
resultado = intercalar_vectores(v1, v2 , True)
print("Resultado de la intercalación:")
mostrar_lista_salteando_valor(resultado )