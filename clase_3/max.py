#ingresar 10 números . Determinar el máximo y el mínimo

#version preguntando si es primera vuelta

for i in range(3):
    numero = float(input("Ingrese un número positivo: "))
    if i==0:
       maximo = numero 
       minimo = numero 
    else:      
       if numero > maximo:
              maximo = numero   
       if numero < minimo:
              minimo = numero     
print(f"Version guardando maximo y minimo en primera vuelta")                      
print(f"El número máximo ingresado es: {maximo}") 
print(f"El número mínimo ingresado es: {minimo}")


#Version inicialiando maximo con -inf
maximo = float('-inf') 
minimo = float('inf')

for i in range(3):
    numero = float(input("Ingrese un número positivo: "))
    if numero > maximo:
        maximo = numero   
    if numero < minimo:
        minimo = numero    
 
print (f"Version con inicializacion de maximos y minimos")    
print(f"El número máximo ingresado es: {maximo}") 
print(f"El número mínimo ingresado es: {minimo}")