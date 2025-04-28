
#Solicitar al usuario que ingrese  números hasta que ingrese 0 . 
# (con 0 terminaría el ingreso)  .
# Calcular la suma de los números ingresados y el promedio de los mismos. 
# y cuantos numeros fueron mayores a 10
#Calcular el valor maximo ingresado

cant_numeros = 0
suma = 0
mayores_a_diez = 0
#inicializo el maximo
#maximo = float('-inf')

numero = float(input("Ingrese un número , o 0 para finalizar el ingreso: "))
while numero != 0:
    if cant_numeros == 0:
        maximo = numero
    else:    
        if numero > maximo:
             maximo = numero 
             
    suma += numero
    cant_numeros += 1
    if numero > 10:
        mayores_a_diez = mayores_a_diez + 1
    #version inciializando maximo
     
       
    numero = float(input("Ingrese un número , o 0 para finalizar el ingreso: "))
    
#imprimo los resultados
if cant_numeros > 0:
    promedio = suma / cant_numeros
    print(f"El promedio de los números ingresados es: {promedio}")  
    print(f"Cantidad de números mayores a 10: {mayores_a_diez}")
    print (f"la suma de los números ingresados es: {suma}")
else:
    print("No se ingresaron números.")