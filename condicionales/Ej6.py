# Enunciado:
# Para ingresar al parque temático Aventura Extrema, se requiere tener al menos 10 años de edad y medir más de 1,40 metros.
# El programa debe permitir ingresar la edad y la estatura de varios niños y determinar si pueden ingresar o no a la atracción.
#Ver tabla de verdad de la operación lógica AND.

# Ingresar la edad y estatura del niño
edad = int(input("Ingrese la edad del niño: "))
estatura = float(input("Ingrese la estatura del niño en metros: "))

# Verificar si cumple con los requisitos para ingresar
if edad >= 10 and estatura > 1.40:
    print("El niño puede ingresar a Aventura Extrema.")
else:
    print("El niño NO puede ingresar a Aventura Extrema.")
