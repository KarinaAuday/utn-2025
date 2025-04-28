#una funcion que no recibe ni devuelve nada
def saludar(nombre , edad):
    print("Hola, bienvenido al programa! " , nombre)
    print("Usted tiene " , edad , " años")

def sumar (numero1 , numero2 ):
    suma = numero1 + numero2
    return suma

def pedir_numero (mensaje):
    numero = float(input(mensaje))
    return numero
def imprimir (valor, texto):
    print(f"{texto}: {valor}")    


#-----------------------------------------------------------
num1 = pedir_numero("Ingrese un número: ")
num2 = pedir_numero("Ingrese otro número: ")
suma_de_dos_numeros = sumar(num1 , num2)
imprimir(suma_de_dos_numeros , "La suma de los dos números es: ")

#nombre = input("Ingrese su nombre: ")
#edad = int(input("Ingrese su edad: "))
#saludar(nombre , edad)
 