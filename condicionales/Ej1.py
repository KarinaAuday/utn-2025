# Enunciado:
# Realizá un programa que permita ingresar 4 notas pertenecientes a tres bimestres distintos para cierto alumno de nivel secundario.
# Debe calcularse y mostrarse la nota promedio.

# Ingresar las notas de los tres bimestres
nota1 = float(input("Ingrese la nota del primer bimestre: "))
nota2 = float(input("Ingrese la nota del segundo bimestre: "))
nota3 = float(input("Ingrese la nota del tercer bimestre: "))
nota4 = float(input("Ingrese la nota del cuarto bimestre: "))

# Calcular la nota promedio
suma = nota1 + nota2 + nota3 + nota4
# Se puede calcular la nota promedio directamente dividiendo la suma entre 4
promedio = (nota1 + nota2 + nota3 + nota4) / 4
# O también se puede calcular la nota promedio dividiendo la suma entre 4
# promedio = suma / 4
# Se puede calcular la nota promedio directamente dividiendo la suma entre 4

# Mostrar el resultado
print(f"La nota promedio del alumno es: {promedio}")
