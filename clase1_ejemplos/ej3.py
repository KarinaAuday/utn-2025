# Ingresar dos números naturales
numero1 = int(input("Ingrese el primer número natural: "))
numero2 = int(input("Ingrese el segundo número natural: "))

# Calcular las 4 operaciones básicas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 != 0:
    division = numero1 / numero2

print(f"Resultado de la suma: {suma}")
print(f"Resultado de la resta: {resta}")
print(f"Resultado de la multiplicación: {multiplicacion}")
if numero2 != 0:
    print(f"Resultado de la división: {division}")
else:
    print("No se puede dividir por cero")
