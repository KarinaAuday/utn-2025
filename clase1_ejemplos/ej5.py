# Enunciado:
# Realizá un programa que permita ingresar tres números
#e indique cual es el mayor y su valor

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: ")) 
numero3 = int(input("Ingrese el tercer número: "))


if numero1 > numero2  and numero1 > numero3:
    mayor = numero1
elif numero2 > numero3:     
    mayor = numero2
else:
    mayor = numero3
    

print(f"el mayor es {mayor}")

    
          
        

