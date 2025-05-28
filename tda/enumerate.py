frutas = ["manzana", "banana","cereza"] 
for i, fruta in enumerate(frutas):
    print(f"Índice: {i}, Fruta: {fruta}")
    
nombres = ["Juan", "Ana", "Pedro", "María"]
edades = [25, 30, 22, 28]
for nombre,edad in zip(nombres, edades):
    print(f"Nombre: {nombre}, Edad: {edad}")