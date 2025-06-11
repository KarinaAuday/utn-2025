import pygame
import sys

pygame.init()
ANCHO = 500
ALTO = 500
COLOR_AMARILLO = (255, 255, 0)
COLOR_CELESTE = (0, 0, 128)
COLOR_BLANCO = (255, 255, 255)
COLOR_ROJO = (255, 0, 0)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Botones con Pygame")

fuente = pygame.font.Font(None, 36)

boton_rect = pygame.Rect(150, 200, 200, 50)

seguir = True

while seguir:
    pantalla.fill(COLOR_BLANCO)
    mouse_pos = pygame.mouse.get_pos()
    if boton_rect.collidepoint(mouse_pos):
       color_boton = COLOR_AMARILLO
    else:
       color_boton = COLOR_CELESTE
    
    pygame.draw.rect(pantalla, color_boton, boton_rect)
    texto_boton = fuente.render("SALIR", True, COLOR_ROJO)
    texto_rect = texto_boton.get_rect(center=boton_rect.center)
    pantalla.blit(texto_boton, texto_rect)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            seguir = False
       
       
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botón izquierdo del mouse
                if boton_rect.collidepoint(evento.pos):
                    print("Botón SALIR presionado")
                    seguir = False
                    
                    
    pygame.display.flip()
pygame.quit()
sys.exit()