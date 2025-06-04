import csv

print ('con wtih')
with open ('prueba.txt', 'r+', encoding='utf-8') as archivo:
     for linea in archivo:
         print(linea, end='')
print('\ncon open')

archivo = open('prueba.txt', 'r+', encoding='utf-8')
print(archivo.read())
archivo.close()

print ('escritura')
archivo = open('prueba2.txt', 'w', encoding='utf-8')
texto = ['Hola, mundo!\n',
         'Este es un archivo de prueba.\n',
         'Estamos escribiendo en él.\n',
         '¡Adiós!\n']
archivo.writelines(texto)   
# Cierra el archivo
archivo.close()
print ('\nlectura')
archivo = open('prueba2.txt', 'r', encoding='utf-8')
print(archivo.read())
archivo.close()
archivo = open('prueba2.txt', 'r', encoding='utf-8')
lineas = archivo.readlines()
for linea in lineas:
    print(linea, end='')  # Imprime cada línea sin agregar una nueva línea adicional    
archivo.close()
#CSV-------------------------------------------------------------------------
with open('ejemplo.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    # Escribir fila por fila
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])
    escritor.writerow(['Ana', '28', 'Madrid'])
    escritor.writerow(['Luis', '35', 'Buenos Aires'])
print ('leer archivo')
with open('ejemplo.csv', 'r', encoding='utf-8') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)  # Imprime cada fila como una lista
print('Guardar archivo en una matriz')

def guardar_en_matriz(archivo_csv):
    matriz = []
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            matriz.append(fila)
    return matriz