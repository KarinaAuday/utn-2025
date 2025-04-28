# Enunciado:
# Para ingresar al parque temático Aventura en el aire, se requiere mas de 12 años de edad o medir más de 1,50 metros.
# El programa debe permitir ingresar la edad y la estatura de varios niños y determinar si pueden ingresar o no a la atracción.
#Ver tabla de verdad de la operación lógica OR
# Ingresar la edad y estatura del niño
edad = int(input("Ingrese la edad del niño: "))
estatura = float(input("Ingrese la estatura del niño en metros: "))

# Verificar si cumple con al menos uno de los requisitos para ingresar
if edad > 12 or estatura >= 1.50:
    print("El niño puede ingresar a  Aventura en el aire.")
else:
    print("El niño NO puede ingresar a Aventura en el aire.")
