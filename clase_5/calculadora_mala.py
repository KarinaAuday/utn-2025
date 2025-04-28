
# calculadora_mala.py

resultado = 0  # ❌ variable global compartida

def sumar(a, b):
    global resultado
    resultado = a + b  # ❌ modifica una variable externa
    
def mostrar():
    print("El resultado es:", resultado)  # ❌ depende de una variable externa

# Uso
mostrar()
sumar(3, 5)

