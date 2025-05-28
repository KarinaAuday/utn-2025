frutas = ["manzana", "banana","cereza"] 
print("Lista original de frutas:", frutas)
frutas.insert(2,"naranja")
print("Lista de frutas después de agregar una nueva:", frutas)
otras_frutas= ["kiwi", "mango"]
frutas.extend(otras_frutas)
print("Lista de frutas después de agregar otras frutas:", frutas)
frutas.remove("kiwi")
print("Lista de frutas después de eliminar una con remove:", frutas)
fruta_eliminada = frutas.pop(1)
print("Lista de frutas después de eliminar una con pop:", frutas)
print("Fruta eliminada con pop:", fruta_eliminada)
posicion = frutas.index("cereza")
print("Posición de 'cereza' en la lista:", posicion)
frutas.sort()
print("Lista de frutas ordenada alfabéticamente:", frutas)
frutas.clear()
print("Lista de frutas después de limpiar:", frutas)

print("--------------------------------------------------------")
ciudades = ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata"]
posicion = ciudades.index("Rosario",1)
print("Lista de ciudades:", ciudades)
#print("Posición de 'Rosario' en la lista:", posicion)
del ciudades[1:3]
print("Lista de ciudades después de eliminar algunas:", ciudades)

numeros = [6,7,1,89,-4]
#numeros.sort()
#print(numeros)
#numeros.reverse()
print(numeros)
numeros.sort(reverse=False)
print(numeros)
del numeros[0]
print("Lista de números después de eliminar el primer elemento:", numeros)
