
#Defino las funciones
def saludar():
    """Imprime un saludo."""
    print("Hola, bienvenido a la calculadora de suma.")

def ingresar_numero(texto):
    """Solicita al usuario que ingrese un número y lo devuelve."""
    numero= float(input(texto))
    return numero 

def sumar (num1, num2):
    """Devuelve la suma de dos números."""
    return num1 + num2
def restar (num1, num2):
    """Devuelve la resta de dos números."""
    return num1 - num2
def multiplicar (num1, num2):
    """Devuelve la multiplicación de dos números."""
    return num1 * num2
def dividir (num1, num2):
    """Devuelve la división de dos números."""
    return num1 / num2

def mostrar_resultados(resultado , operacion):
    """Muestra el resultado de la calculadora."""
    print(f"el resultado de la operacion {operacion} es : {resultado}")
    
def ingresar_operacion():
    """Solicita al usuario que ingrese una operación."""
    operacion = input("Ingrese la operación deseada (+, -, *, /) o 'F' para finalizar: ")
    operacion_correcta = operacion == '+' or operacion == '-' or operacion == '*' or operacion == '/' or operacion.upper() == 'F'
    while not operacion_correcta: 
        print("Operación no válida. Por favor, ingrese una operación válida.")
        operacion = input("Ingrese la operación deseada (+, -, *, /) o 'F' para finalizar: : ")
        operacion_correcta = operacion == '+' or operacion == '-' or operacion == '*' or operacion == '/' or operacion.upper() == 'F'
    #validar que la operacion sea correcta
    return operacion

def puede_hacer_operacion(numero , operacion):
    """Verifica si se puede realizar la operación."""
    puede = True
    if (operacion == '/' and numero == 0) :
        puede = False
    return puede


def calculadora (num1, num2 , operacion):
    resultado = None
    match operacion:
        case '+':
            resultado = sumar(num1 , num2)
        case '-':
            resultado = restar(num1 , num2)
        case '*':
            resultado = multiplicar(num1 , num2)
        case '/':
            resultado = dividir(num1 , num2)
        
    return resultado   
   
   
#programa principal-----------------------------------------    
saludar()
operacion = ingresar_operacion()
while operacion.upper() != 'F':
    numero1 = ingresar_numero("Hola, ingresame el primer numero ")
    numero2 = ingresar_numero("Muchas gracias, ahora por favor ingresa el segundo numero ")
    puede = puede_hacer_operacion(numero2 , operacion)
    if puede:
        resultado = calculadora(numero1 , numero2 , operacion )  
        mostrar_resultados(resultado , operacion) 
    else :
         print("No se puede realizar la operación.")   
    
    operacion = ingresar_operacion() 


print ("Gracias por usar la calculadora. ¡Hasta luego!")       