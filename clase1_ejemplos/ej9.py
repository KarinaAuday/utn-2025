num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación deseada (+, -, *, /): ")
resultado = None

match operacion:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("No se puede dividir por cero")
    case _:         
        print("Operación no válida")
        
 
        if operacion == '+' and operacion = "-":
            print (f"El resultado de la operación {operacion} es: {resultado}")    
        elif operacion == '-':
            print (f"El resultado de la operación {operacion} es: {resultado}")    
        elif operacion == '*':
            print (f"El resultado de la operación {operacion} es: {resultado}")    
        elif operacion == '/':
            
        
print (f"El resultado de la operación {operacion} es: {resultado}")    
#     # Operador ternario