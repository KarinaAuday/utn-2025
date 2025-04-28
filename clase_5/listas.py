def modificar_lista(lista):
    """
    Modifica la lista de entrada y devuelve una nueva lista con los elementos modificados.
    """
    print(f"ID dentro de la función antes de modificar: {id(lista)}")
    print ("valor lista",lista)
    lista.append(100)  # Modifica la lista original
    print(f"ID dentro de la función después de modificar: {id(lista)}")
    print ("valor lista",lista)
    
    # Lista original
mi_lista = [1, 2, 3]

print(f"ID original fuera de la función: {id(mi_lista)}")  # ID de la lista antes de la función
print ("valor lista",mi_lista)
modificar_lista(mi_lista)  # Llama a la función con la lista
print(f"ID después de la función: {id(mi_lista)}")  # ID de la lista después de la función
print ("valor lista",mi_lista)  # La lista original ha cambiado