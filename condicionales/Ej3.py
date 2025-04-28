# Enunciado:
# Realizá un programa que permita ingresar dos números naturales.
# Debes mostrar los resultados para las 4 operaciones matemáticas básicas con los números ingresados.

# Ingresar dos números naturales
numero1 = int(input("Ingrese el primer número natural: "))
numero2 = int(input("Ingrese el segundo número natural: "))

# Calcular las 4 operaciones básicas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"

# Mostrar los resultados
print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(f"La división de {numero1} y {numero2} es: {division}")
