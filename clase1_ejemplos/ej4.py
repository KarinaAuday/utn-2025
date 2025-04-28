# Enunciado:
# Realizá un programa que permita ingresar un número entero e indique si se trata de un número par o impar.

# Ingresar el número entero

numero = int(input("Ingrese un número entero: "))
es_par = numero % 2 == 0
if es_par:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
    