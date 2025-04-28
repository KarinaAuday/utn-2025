# calculadora_buena.py

def sumar(a, b):
    resultado = a + b
    return resultado  # ✅ devuelve el valor, no lo guarda en una variable global

def mostrar(valor):
    print("El resultado es:", valor)  # ✅ usa el valor recibido, no depende de variables externas

# Uso
res = sumar(3, 5)
mostrar(60)
