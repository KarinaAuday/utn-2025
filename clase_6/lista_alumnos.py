
def promedio_calificaciones(calificaciones)->float:
    suma = 0
    for i in range(len(calificaciones)):
        suma += calificaciones[i]
    promedio = suma / len(calificaciones)
    return promedio




calificaciones = [10, 5, 9, 7, 2, 4, 6, 9, 10, 2]
promedio_calificaciones = promedio_calificaciones(calificaciones)
print(f"El promedio de calificaciones es: {promedio_calificaciones:.2f}")  # Imprime el promedio de calificaciones




 