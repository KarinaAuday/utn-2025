import pygame

RUTA_IMAGEN = "utn-2025/mario.png"
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
AZUL = (0,0,255)

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

mario = pygame.image.load(RUTA_IMAGEN)
mario = pygame.transform.scale(mario, (150, 150))
#mario.convert_alpha()

pygame.init()

seguir = True

x_mario = 0
y_mario = 0

reloj = pygame.time.Clock()
delta = 0.1

while seguir:
    pantalla.fill(AZUL)
    pantalla.blit(mario, (x_mario,y_mario))

    x_mario += 50 * delta
    y_mario += 50 * delta
    if x_mario > ANCHO_PANTALLA:
        x_mario = 0
    if y_mario > ALTO_PANTALLA:
        y_mario = 0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            seguir = False

    pygame.display.update()

    delta = reloj.tick(60) / 1000.0