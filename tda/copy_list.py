import copy

print("----Shallow Copy")
lista_original = [[1,2], [3,4], [5,6]]
lista_copia = copy.copy(lista_original)
print("Lista original:", lista_original)
print("Lista copia:", lista_copia)
lista_copia[0][0] = 99

print("Lista original :", lista_original)
print("Lista copia:", lista_copia)

print("----Deep Copy")
lista_original2 = [[1,2], [3,4], [5,6]]
lista_copia2 = copy.deepcopy(lista_original2)
print("Lista original:", lista_original2)
print("Lista copia:", lista_copia2)
lista_copia2[0][0] = 99
print("Lista original :", lista_original2)
print("Lista copia:", lista_copia2)