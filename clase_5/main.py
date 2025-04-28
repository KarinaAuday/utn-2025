import paquete1.validaciones as v
def comparar_texto(mensaje , texto)->bool:
    entrada = input(mensaje)
    texto_valido= False
    """Compara dos textos."""
    if entrada == texto:
        texto_valido = True

    return texto_valido
# Este módulo contiene funciones para validar entradas de usuario.
# -*- coding: utf-8 -*-

""" valida texto y numeros en rango """ 
texto = v.validar_texto("Ingrese un texto: ")
print(f"El texto ingresado es: {texto}")
numero_entero = v.validar_entero("Ingrese un número entero: ", 1, 10)
print(f"El número entero ingresado es: {numero_entero}")    
numero_decimal = v.validar_decimal("Ingrese un número decimal: ", 1.0, 10.0)
print(f"El número decimal ingresado es: {numero_decimal}")
legajo_valido = v.legajo_valido("Ingrese un legajo: ", 4 , 0,0)
if legajo_valido:
    print("El legajo es válido.")
else:
    print("El legajo no es válido.")
ocupacion = v.validar_texto("Ingrese su ocupación: estudiante , empleado , empresario , jublilado , desocupado: ")
print(f"La ocupación ingresada es: {ocupacion}")
es_estudiante = comparar_texto("Ingrese su ocupación: estudiante , empleado , jublilado , desocupado: ", "estudiante")
es_empleado = comparar_texto("Ingrese su ocupación: estudiante , empleado , jublilado , desocupado: ", "empleado")
es_jubilado = comparar_texto("Ingrese su ocupación: estudiante , empleado , jublilado , desocupado: ", "jubilado")
es_desocupado = comparar_texto("Ingrese su ocupación: estudiante , empleado , jublilado , desocupado: ", "desocupado")
while not (es_estudiante or es_empleado or es_jubilado or es_desocupado):
    print("Ocupación no válida. Intente nuevamente.")
    ocupacion = v.validar_texto("Ingrese su ocupación: estudiante , empleado , jublilado , desocupado: ")
    es_estudiante = comparar_texto("Ingrese su ocupación: estudiante , empleado , jublilado , desocupado: ", "estudiante")
    es_empleado = comparar_texto("Ingrese su ocupación: estudiante , empleado , jublilado , desocupado: ", "empleado")
    es_jubilado = comparar_texto("Ingrese su ocupación: estudiante , empleado , jublilado , desocupado: ", "jubilado")
    es_desocupado = comparar_texto("Ingrese su ocupación: estudiante , empleado , jublilado , desocupado: ", "desocupado")
print(f"La ocupación ingresada es: {ocupacion}")