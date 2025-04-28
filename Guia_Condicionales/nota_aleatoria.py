import random

nota = random.randint(1, 10)  # Número entre 1 y 10 (incluidos)
print(f"La nota ingresada es : {nota}")
match nota:
    case 6 | 7 | 8 | 9 | 10:
        print(f"Promoción directa, la nota es {nota}")
    case 4 | 5:
        print(f"Aprobado, la nota es {nota}")
    case 1 | 2 | 3:
        print(f"Desaprobado, la nota es {nota}")
    