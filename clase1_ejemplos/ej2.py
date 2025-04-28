# Enunciado:
# Realizá un programa que permita ingresar valores del mismo tipo para las variables valor1 y valor2.
# Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores (que lo cargado en valor1 quede en valor2, y viceversa)
# y volvé a mostrarlas actualizadas.

texto1 = input("INgrese el primer texto: ")
texto2 = input("Ingrese el segundo texto: ")

print(f"Texto 1: {texto1}")
print(f"Texto 2: {texto2}")

texto1, texto2 = texto2, texto1  # Intercambio de valores

print(f"despues de intercambiar Texto 1: {texto1}")
print(f"despues de intercambiar Texto 2: {texto2}")
