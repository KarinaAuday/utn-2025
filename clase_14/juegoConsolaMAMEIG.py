import random

MAX_JUGADORES = 5
MAX_INTENTOS = 3
MIN_NUMERO = 1
MAX_NUMERO = 100

historial_predicciones = []
jugadores_ganadores = []

for i in range(MAX_JUGADORES):
    nombre = input(f"Ingrese el nombre del jugador {i + 1}: ")
    print (f"Bienvenido {nombre} al juego de adivinanza de números!")
    numero_anterior = random.randint(MIN_NUMERO, MAX_NUMERO)
    print (f"Numero Inicial : {numero_anterior}")
    intentos = 0
    adivino = False
    predicciones_jugador = []
    
    while not adivino and intentos < MAX_INTENTOS:
        prediccion = input(f"Intento {intentos + 1} - {nombre}, El proximo numero sera MA , ME o IG (mayor, menor o igual)?").strip().upper()
        while prediccion not in ["MA", "ME", "IG"]:
            prediccion = input(f"Entrada no valida. Intento {intentos + 1} - {nombre}, El proximo numero sera MA , ME o IG (mayor, menor o igual)?").strip().upper()
        nuevo_numero = random.randint(MIN_NUMERO, MAX_NUMERO)  
        predicciones_jugador.append((prediccion))
        if nuevo_numero > numero_anterior:
           resultado_real = "MA"
        elif nuevo_numero < numero_anterior:
            resultado_real = "ME"   
        else:
            resultado_real = "IG"

        print (f"El numero que salio es  {nuevo_numero} ")
        if prediccion == resultado_real:
           adivino = True
           jugadores_ganadores.append(nombre)
           print (f"¡Felicidades {nombre}, adivinaste correctamente!") 
        else:
           print (f"Lo siento {nombre}, no adivinaste la prediccion. El resultado real era {resultado_real}.")
           numero_anterior = nuevo_numero
        intentos += 1 
          
    while len(predicciones_jugador) < MAX_INTENTOS:
        predicciones_jugador.append("GANO")       
        
    historial_predicciones.append((predicciones_jugador))        
    
    
    #mostrar resultados
print(f"\nResultados de {nombre}:")
for intento , fila in enumerate (historial_predicciones):
    print(f"Jugador {intento + 1}: {fila}")
       
for ganador in jugadores_ganadores:
    print(f"Jugador ganador: {ganador}")       