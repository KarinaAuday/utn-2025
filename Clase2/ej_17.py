#acumulador
suma_sueldos = 0
#contador
sueldos_mayores_diezmil = 0

cant_sueldos = int(input("Ingrese la cantidad de sueldos a cargar: "))

for i in range(cant_sueldos):
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    suma_sueldos += sueldo
    if sueldo > 10000:
        sueldos_mayores_diezmil +=1 
promedio = suma_sueldos / cant_sueldos
print(f"El promedio de los sueldos es: {promedio}")
print(f"La cantidad de sueldos mayores a 10.000 es: {sueldos_mayores_diezmil}")    