def sumar (a,b):
    return a + b

def restar (a,b):
    return a - b

def multiplicar (a,b):
    return a * b


#-# Ejemplo de funciones como objetos de primera clase
print("Funciones como objetos de primera clase")
operacion = sumar

print("sumo ", operacion(2,3))

muchas_operaciones = [sumar, restar, multiplicar]

for operacion in muchas_operaciones:
    print("muchas operaciones en lista" ,operacion(2,3))
    
muchas_operaciones2 = (sumar, restar, multiplicar)
print("---------------------------------------------------------------")

resultado_suma = muchas_operaciones2[0](2,3)
print("resultado suma en tupla", resultado_suma)    
resultado_resta = muchas_operaciones2[1](2,3)
print("resultado resta en tupla ", resultado_resta)

muchas_operaciones3 = {
    "suma": sumar,
    "resta": restar,
    "multiplicacion": multiplicar
}
print("---------------------------------------------------------------")

resultado_suma = muchas_operaciones3["suma"](2,3)
print("resultado suma en diccionario", resultado_suma)
resultado_resta = muchas_operaciones3["resta"](2,3)
print("resultado resta en diccionario ", resultado_resta)
resultado_multiplicacion = muchas_operaciones3["multiplicacion"](2,3)
print("resultado multiplicacion en diccionario ", resultado_multiplicacion)


#-# Ejemplo de funciones como parametros de otras funciones
print("Funciones como parametros de otras funciones")
def operar (a , b, funcion):
    return funcion(a,b)
print("---------------------------------------------------------------")

resultado_suma = operar(2,3,sumar)
print("resultado suma con funcion como parametro", resultado_suma)
resultado_resta = operar(2,3,restar)
print("resultado resta con funcion como parametro ", resultado_resta)
resultado_multiplicacion = operar(2,3,multiplicar)
print("resultado multiplicacion con funcion como parametro ", resultado_multiplicacion)

def aplicar_operacion (numero , funcion):
    resultado =  funcion(numero)
    return resultado

def duplicar(x):
    return x * 2
    
def triplicar(x):
    return x * 3

#usando la funcion aplicar_operacion
print("---------------------------------------------------------------")

resultado1 = aplicar_operacion(5, duplicar)
print("resultado duplicar con funcion como parametro", resultado1)   
resultado2 = aplicar_operacion(5, triplicar)
print("resultado triplicar con funcion como parametro", resultado2) 

print("---------------------------------------------------------------")
#-# Ejemplo de funciones que toma otra funcion como parametro
def ordenar_lista(lista, funcion):
    lista.sort(key=funcion)
    return lista
def ordenar_por_longitud(palabra):
    return len(palabra)

palabras = ["Python", "Java", "C++", "JavaScript", "Ruby"]
print("Lista original:", palabras)
palabras_ordenadas = ordenar_lista(palabras, ordenar_por_longitud)
print("Lista ordenada por longitud:", palabras_ordenadas)    
print("---------------------------------------------------------------")
#funciones que retornan otras funciones
def funcion_externa(x):
    return x + 5

def retornar_funcion():
    return funcion_externa
# Usando la funcion retornar_funcion
mi_funcion = retornar_funcion()    

#usar la funcion retornada
resultado = mi_funcion(10)  
print("Resultado de la funcion retornada:", resultado)  # Resultado: 15

print("---------------------------------------------------------------")
#funciones Lambda
# Definición de una función lambda para sumar dos números
suma_lambda = lambda a, b: a + b
print("Suma", suma_lambda(2, 3))
suma2 = (lambda a, b ,c : a + b + c)(5, 3 , 4)
print("Suma con tres parametros", suma2)


print("---------------------------------------------------------------")
def validar(valor,condicion):
   return condicion(valor)

es_positivo = lambda x: x > 0
print("Validar si es positivo", validar(5, es_positivo))  # True
print("Validar si es negativo", validar(-5, es_positivo))  # False
