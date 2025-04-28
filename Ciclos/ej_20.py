import sys
numero = float(input("Ingrese un numero o 0 para finalizar: "))
mayor = sys.float_info.min
menor = sys.float_info.max
contador = 0

while numero != 0:
    if numero > mayor:
        mayor = numero
    elif numero < menor:
        menor = numero
    contador += 1
    # Solicitar otro número    
    numero = float(input("Ingrese un numero o 0 para finalizar: "))
print(f"El mayor numero ingresado es: {mayor}")
print(f"El menor numero ingresado es: {menor}")
print(f"Se ingresaron {contador} numeros")
# Se utiliza sys.float_info.min y sys.float_info.max para garantizar que los valores iniciales de mayor y menor sean válidos
# El programa termina cuando se ingresa 0

