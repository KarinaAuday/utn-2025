def cuenta_regresiva_for (numero):
    for i in range (numero , 0 , -1):
        print (i)
        
def cuenta_regresiva_recursiva (numero):
    print (numero)  
    if numero > 1:
        # Llamada recursiva
       cuenta_regresiva_recursiva (numero - 1)      
        
#Funcion que suma todos los numeros desde 1 hasta el numero ingresado
# si le mando 5    ..5 
# + 4 + 3 + 2 + 1 = 15 
def sumatoria_for (numero):
    suma = 0
    for i in range (numero , 0 , -1):
        suma += i
    return suma

def sumatoria_recursiva (numero):
    resultado = 0
    if numero > 0:
       resultado = numero + sumatoria_recursiva (numero - 1)
    return resultado

def calcular_factorial (numero):
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial (numero - 1)
        
    return resultado
    
resultado_factorial = calcular_factorial (5)
print (resultado_factorial)    
#suma_recu = sumatoria_recursiva (5)
#print (suma_recu)
#sumatoria = sumatoria_for (5) 
#print (sumatoria) 
        
#cuenta_regresiva_for (10)        
##cuenta_regresiva_recursiva (5)