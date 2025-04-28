# Enunciado:
# Realizá un programa que permita ingresar valores del mismo tipo para las variables valor1 y valor2.
# Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores (que lo cargado en valor1 quede en valor2, y viceversa)
# y volvé a mostrarlas actualizadas.

# Ingresar los valores para valor1 y valor2
valor1 = input("Ingrese el valor para valor1: ")
valor2 = input("Ingrese el valor para valor2: ")

# Mostrar los valores originales
print(f"Valor1: {valor1}")
print(f"Valor2: {valor2}")

# Intercambiar los valores utilizando una variable auxiliar
auxiliar = valor1
valor1 = valor2
valor2 = auxiliar

# Mostrar los valores después del intercambio
print(f"Valor1 después del intercambio: {valor1}")
print(f"Valor2 después del intercambio: {valor2}")

# Intercambiar los valores de valor1 y valor2 como permite python
#valor1, valor2 = valor2, valor1

# Mostrar los valores después del intercambio
#print(f"Valor1 después del intercambio: {valor1}")
#print(f"Valor2 después del intercambio: {valor2}")
