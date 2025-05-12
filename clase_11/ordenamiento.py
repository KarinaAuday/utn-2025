def burbuja(lista:list) -> list:
    n = len(lista)
    for i in range(n):
        for j in range(0, n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def burbuja_mejorado(lista:list) -> list:
    n = len(lista)
    i = 0
    intercambiado = True
    while i < n and intercambiado:
        intercambiado = False
        for j in range(0, n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        i += i
    return lista

def seleccion(lista:list) -> list:
    n = len(lista)
    aux = 0
    for i in range(n):
        num_mas_chico = i
        for j in range(i+1, n):
            if lista[j] < lista[num_mas_chico]:
                num_mas_chico = j
        #i -> num_mas_chico, num_mas_chico -> i
        aux = lista[num_mas_chico]
        lista[num_mas_chico] = lista[i]
        lista[i] = aux
    return lista

def quick_sort(lista:list) -> list:
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores_pivote = []
    mayores_pivote = []

    for i in range(1, len(lista)):
        if lista[i] <= pivote:
            menores_pivote.append(lista[i])
        else:
            mayores_pivote.append(lista[i])

    lista_menores = quick_sort(menores_pivote)
    lista_mayores = quick_sort(mayores_pivote)

    lista_resultado = []

    for elemento in lista_menores:
        lista_resultado.append(elemento)
    lista_resultado.append(pivote)
    for elemento in lista_mayores:
        lista_resultado.append(elemento)

    return lista_resultado