import random

MAX_JUGADORES = 5
MAX_INTENTOS = 3

matriz_predicciones = []  # Matriz 5x3 con las predicciones de los jugadores
jugadores_ganadores = []  # Lista para almacenar los nombres de los jugadores ganadores
for j in range(MAX_JUGADORES):
    nombre = input(f"Ingrese el nombre del jugador #{j + 1}: ")
    print(f"\nTurno de {nombre}")
    
    predicciones_jugador = []  # Lista temporal para este jugador
    numero_anterior = random.randint(1, 20)
    print(f"Número inicial: {numero_anterior}\n")
    
    intento = 0
    seguir_jugando = True

    while intento < MAX_INTENTOS and seguir_jugando:
        prediccion = input(f"Intento {intento + 1} - ¿El próximo número será MA, ME o IG?: ").strip().upper()
        while prediccion not in ["MA", "ME", "IG"]:
            prediccion = input("Entrada inválida. Ingrese MA, ME o IG: ").strip().upper()

        nuevo_numero = random.randint(1, 20)
        print(f"Número generado: {nuevo_numero}")

        # Guardamos la predicción con append
        predicciones_jugador.append(prediccion)

        # Comparar con el anterior
        if nuevo_numero > numero_anterior:
            resultado_real = "MA"
        elif nuevo_numero < numero_anterior:
            resultado_real = "ME"
        else:
            resultado_real = "IG"
          
        if prediccion == resultado_real:
            print("¡Acierto!\n")
            numero_anterior = nuevo_numero
            seguir_jugando = False
            jugadores_ganadores.append(nombre)  # Agregar el nombre del jugador ganador
        else:
            print("Fallaste. Fin de tu turno.\n")
        

        intento += 1

    # Si hizo menos de 3 predicciones, rellenamos con string vacío
    while len(predicciones_jugador) < MAX_INTENTOS:
        predicciones_jugador.append("GANO")

    matriz_predicciones.append(predicciones_jugador)

# Mostrar matriz final
print("\n--- MATRIZ DE PREDICCIONES (5 jugadores x 3 intentos) ---")
for idx, fila in enumerate(matriz_predicciones, start=1):
    print(f"Jugador #{idx}: {fila}")

for jugadores in jugadores_ganadores:
    print(f"Jugador ganador: {jugadores}")