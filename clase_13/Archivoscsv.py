import csv

with open('ejemplo.csv', 'r') as archivo_csv:
     lineas = archivo_csv.readlines()
     #cant_filas = len(lineas)
    # cant_columnas = len(lineas[0].strip().split(','))
     
     matriz = []
     for linea in lineas:
        fila = linea.strip().split(',')
        matriz.append(fila)
    
     for fila in matriz:
        print(fila)  # Imprime cada fila como una lista    