# Enunciado:
# Realizá un programa que permita ingresar 4 notas pertenecientes a 4 bimestres distintos para cierto alumno de nivel secundario.
# Debe calcularse y mostrarse la nota promedio.

CANT_BIMESTRES = 4
nota1 = float(input("ingrese la nota del primer bimestre: "))
nota2 = float(input("ingrese la nota del segundo bimestre: "))
nota3 = float(input("ingrese la nota del tercer bimestre: "))
nota4 = float(input("ingrese la nota del cuarto bimestre: "))

suma = nota1 + nota2 + nota3 + nota4
promedio = suma / CANT_BIMESTRES
print(f"La nota promedio es: {suma / CANT_BIMESTRES}")


