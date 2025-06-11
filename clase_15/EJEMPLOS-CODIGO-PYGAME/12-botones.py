import pygame

# Definimos una función para crear botones
def crear_boton(ventana, posicion, fuente=None, texto=None, imagen=None):
    boton = {}
    boton['ventana'] = ventana
    boton['posicion'] = posicion
    boton['texto'] = texto
    boton['fuente'] = fuente

    if imagen is None:
        sup_imagen = pygame.image.load('mosca.png')
    else:
        sup_imagen = pygame.image.load(imagen)

    sup_imagen = pygame.transform.scale(sup_imagen, (100, 100))
    boton['imagen'] = sup_imagen

    rect = boton['imagen'].get_rect()
    rect.topleft = posicion
    boton['rect'] = rect

    return boton

# Función para dibujar el botón
def dibujar(boton):
    ventana = boton["ventana"]
    ventana.blit(boton['imagen'], boton['posicion'])
    if boton['texto'] is not None:
        texto = boton['fuente'].render(boton['texto'], True, (0, 0, 0))
        rect_texto = texto.get_rect(center=boton['rect'].center)
        ventana.blit(texto, rect_texto)

# Iniciamos Pygame
pygame.init()

# Creamos la ventana
ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Botones con Funcionalidad")
icono = pygame.image.load('mosca.png')
pygame.display.set_icon(icono)

# Fondo de pantalla
imagen_fondo = pygame.image.load('fondo.jpg')
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500))

# Creamos los botones
boton1 = crear_boton(ventana, (200, 200), fuente=pygame.font.Font(None, 36), texto="Click Me")
boton2 = crear_boton(ventana, (100, 100), fuente=pygame.font.Font(None, 36), texto="Salir", imagen="mosca.png")

# Colores
COLOR_BLANCO = (255, 255, 255)

# Control del bucle
corriendo = True

# Bucle principal
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        # Detectamos clic con el mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_click = pygame.mouse.get_pos()  # Obtiene la posición del clic

            # Si el clic fue sobre boton1
            if boton1['rect'].collidepoint(pos_click):
                boton1['texto'] = "¡Pulsado!"  # Cambiamos su texto

            # Si el clic fue sobre boton2
            if boton2['rect'].collidepoint(pos_click):
                corriendo = False  # Salimos del bucle y cerramos

    # Dibujamos fondo
    ventana.blit(imagen_fondo, (0, 0))

    # Dibujamos botones
    dibujar(boton1)
    dibujar(boton2)

    # Actualizamos pantalla
    pygame.display.update()

# Cerramos Pygame
pygame.quit()
