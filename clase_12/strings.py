cadena = "él dijo: \"me gusta la letra 'a'\"\nacá hay otra línea de texto."
#print(cadena[5])
#print(cadena[9])
#print(cadena[32])
#print(cadena[35])
#cadena[5] = 'x' LAS CADENAS SON INMUTABLES
#print(cadena[10:31])
#print("La longitud de la cadena es", len(cadena))
#print("ID de la cadena antes de concatenar:", id(cadena))
cadena += " Este texto sigue al lado del anterior."
#print(cadena)
#print("Ahora la longitud es",len(cadena))
#print("ID de la cadena después de concatenar:", id(cadena))

#print(cadena * 10)

#palabra1 = "Procesador"
#palabra2 = "procesador"

#palabra1 = palabra1.lower()
#palabra2 = palabra2.lower()
#print(palabra2)

#print(palabra1 == palabra2)
#print(palabra1 > palabra2)
#print(palabra1 < palabra2)
#print(palabra1 != palabra2)
contadorA = 0
for i in range(len(cadena)):
    if cadena[i] == 'a':
        contadorA += 1

cadenaNueva = ""
cadenaAux = ""

for i in range(len(cadena)):
    if(i == 0):
        cadenaNueva = cadena[i]
        cadenaNueva = cadenaNueva.upper()
    if(cadena[i] == '"' or cadena[i] == '\n'):
        cadenaAux = cadena[i+1]
        cadenaAux = cadenaAux.upper()
        cadenaNueva += cadenaAux
    elif(cadena[i - 1] != '"' and cadena[i - 1] != '\n' and i != 0):
        cadenaNueva += cadena[i]

print(cadenaNueva)

def validar_rango(n, minimo, maximo):
    ret = True
    while n < minimo or n > maximo:
        print("Número fuera de rango. Ingresalo de nuevo:")
        n = int(input("n = "))
        ret = False
    return ret

def validar_rango(n, minimo, maximo):
    ret = False
    while n < minimo or n > maximo:
        print("Número fuera de rango. Ingresalo de nuevo:")
        n = int(input("n = "))
    return ret

def validar_rango(n, minimo, maximo):
    ret = False
    while n >= minimo or n <= maximo:
        print("Número fuera de rango. Ingresalo de nuevo:")
        n = int(input("n = "))
        ret = True
    return ret

def validar_rango(n, minimo, maximo):
    ret = True
    while n < minimo:
        print("Número fuera de rango. Ingresalo de nuevo:")
        n = int(input("n = "))
        ret = False
    return ret

def validar_rango(n, minimo, maximo):
    while n < minimo or n > maximo:
        print("Número fuera de rango. Ingresalo de nuevo:")
        n = int(input("n = "))
    return True