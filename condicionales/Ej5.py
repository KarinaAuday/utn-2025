# Enunciado:
# Realizá un programa que permita ingresar dos números e indique cual es el mayor y su valor

# Ingresar el número entero
numero1 = int(input("Ingrese un número : "))
# Ingresar el número entero
numero2 = int(input("Ingrese otro número : "))
# Verificar si el número es par o impar

if numero1 > numero2:
    mayor = numero1
elif numero1 < numero2:
   mayor = numero2
else:
    print(f"Los números {numero1} y {numero2} son iguales.")

print(f"El número mayor es {mayor}.")