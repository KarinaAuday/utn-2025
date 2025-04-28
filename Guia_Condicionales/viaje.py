estacion = input("Ingresa la estación del año: ").lower()  # Pedimos la estación y la pasamos a minúsculas

match estacion:
    case "invierno":
        print("Se viaja a Bariloche")  # Solo Bariloche
    case "verano":
        print("Se viaja a Mar del Plata y Cataratas")  # Mar del Plata y Cataratas
    case "otoño":
        print("Se viaja a Bariloche, Mar del Plata y Cataratas")  # Todos los lugares
    case "primavera":
        print("Se viaja a Mar del Plata y Cataratas")  # Todos menos Bariloche
    case _:
        print("Estación no válida")  # Si la estación no es válida
