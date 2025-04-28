#int paso del valor de la variable a la funcion
def modificar_numero (numero):
    """Modifica el valor de la variable pasada como argumento."""
    print ("ID de la variable original en la Funcion modificar_numero:", id(numero)) 
    print ("Valor de la variable original en la Funcion modificar_numero", numero)
    numero += 10  # Modifica el valor localmente, pero no afecta al original
    print("ID después dentro de la función modificar_numero:", id(numero))
    print("Valor después dentro de la función modificar_numero:", numero)

numero_main = 5
print("ID de la variable original en el main:", id(numero_main))
print("Valor de la variable original en el main:", numero_main)
modificar_numero(numero_main)  # Llama a la función con el número
print("ID después de la función en el main:", id(numero_main))
print("Valor después de la función en el main:", numero_main)  # El valor original no cambia