edad = int(input("Ingrese la edad del niño: "))
estatura = float(input("Ingrese la estatura del niño en metros: "))
EDAD_MINIMA = 10
ALTURA_MIN = 1.40
puede_entrar = edad >= EDAD_MINIMA and estatura > ALTURA_MIN

if puede_entrar:
    print("El niño puede participar en el juego")
else:
    print("El niño no puede participar en el juego")
    
    #  AND  
    # V and V = V
    # V and F = F
    # F and V = F
    # F and F = F  
    
    #OR
    # V or V = V
    # V or F = V
    # F or V = V
    # F or F = F  