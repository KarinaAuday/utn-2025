numero = int(input("Ingrese un número (0 para terminar): "))
suma_negativos = 0
suma_positivos = 0
cantidad_positivos = 0
cantidad_negativos = 0
max_positivo = 0
minimo = float('inf') 


while numero != 0:
    #calculo minimo
    if numero < minimo:
        minimo = numero
    #numeros negativos
    if numero < 0:
        suma_negativos += numero
        cantidad_negativos += 1 
    else:
        suma_positivos += numero
        cantidad_positivos += 1 
        #calculo maximo
        if numero > max_positivo:
            max_positivo = numero       
    numero = int(input("Ingrese un número (0 para terminar): "))


#imprimo resultados
if cantidad_positivos > 0:
    promedio_positivos = suma_positivos / cantidad_positivos
    print(f"El promedio de los números positivos ingresados es: {promedio_positivos}") 
    print(f"Cantidad de números positivos ingresados: {cantidad_positivos}")
    print(f"El número máximo positivo ingresado es: {max_positivo}")
else:
    print("No se ingresaron números positivos.")   
    
print (f"Cantidad de números negativos ingresados: {cantidad_negativos}")
print (f"La suma de los números negativos ingresados es: {suma_negativos}")
if minimo != float('inf'):
  print (f"El número mínimo ingresado es: {minimo}")      
else:
  print("No se ingresaron números")            