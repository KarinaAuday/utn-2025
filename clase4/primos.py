
def ingresar_numero(texto):
    """Solicita al usuario que ingrese un número y lo devuelve."""
    numero= int(input(texto))
    return numero 

def es_primo(numero):
    #Tengo que probar si es divisible por 2, 3, 4, ....todos los numeros hasta el numero ingresado menos 1
    resultado = True
    contador = 2
    if numero > 1:
        #si el numero es menor a 2 no es primo
        while (contador < numero - 1) and resultado == True:
            if numero % contador == 0:
                resultado = False
            contador = contador + 1    
    return resultado    

#programa principal

num = ingresar_numero("Ingrese un numero: ")
es_numero_primo = es_primo(num)
if es_numero_primo:
    print(f"El número {num} es primo.")
else:   
    print(f"El número {num} no es primo.")