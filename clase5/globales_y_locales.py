suma_total = 0

#Version con variable Global
def sumar_hasta_global(n , nombre):
    global suma_total  # Indicamos que vamos a usar la variable global
    print (f"Hola {nombre}")
    for i in range(1, n + 1):
        suma_total += i

def sumar_hasta_local(n):
    suma_local = 0  # Variable local
    for i in range(1, n + 1):
        suma_local += i
    return suma_local
def saludar (nombre):
    print (f"Hola {nombre}")
    
nombre = input("Ingrese su nombre: ")
sumar_hasta_global(3, "Karina")  # SUMA CON ARIABLE GLOBAL

print("La sumatoria Global es:", suma_total)
#---------------------------------------------------------------
nombre = input("Ingrese su nombre: ")
saludar(nombre)
suma_local = sumar_hasta_local(3)  # SUMA CON VARIABLE LOCAL
print ("La sumatoria Local es:",suma_local)

