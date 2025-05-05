
from validaciones_2 import validar_int_en_rango
def buscar_numero(lista, valor) ->bool:
    i = 0
    encontrado = False
    while i < len(lista) and not encontrado:
        if lista[i] == valor:
            encontrado = True
        i += 1
    return encontrado



def sumatoria(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def encontrar_mayor(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador

def mostrar_menu ():
    print ("Bienvenido al menú de usuario")
    print ("1. Buscar un número en la lista")
    print ("2. Calcular la sumatoria de la lista")
    print ("3. Encontrar el mayor número de la lista")
    print ("4. Contar los números pares en la lista")
    print ("5. Salir")



# Programa principal
print("Bienvenido al programa")
mostrar_menu()
opcion = int(input("Seleccione una opción (1-5): "))
lista = [1, 2, 3, 4, 5]
while opcion != 5:
    match opcion:
        case 1:
            numero = int(input("Ingrese el número a buscar: "))

            if buscar_numero(lista, numero):
                print(f"El número {numero} se encuentra en la lista.")
            else:
                print(f"El número {numero} no se encuentra en la lista.")
        case 2:
            total = sumatoria(lista)
            print(f"La sumatoria de la lista es: {total}")
        case 3:
            mayor = encontrar_mayor(lista)
            print(f"El mayor número de la lista es: {mayor}")
        case 4:
            cantidad_pares = contar_pares(lista)
            print(f"La cantidad de números pares en la lista es: {cantidad_pares}")    
        case _:
            print("Opción no válida. Intente nuevamente.")    
            
    input("Presione Enter para continuar...")    
    mostrar_menu()            
    opcion = int (input("Seleccione una opción (1-5): "))
print("Gracias por usar el programa. ¡Hasta luego!")   
