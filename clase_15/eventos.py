import pygame
pygame.init()

ANCHO = 500
ALTO = 500
COLOR_AMARILLO = (255,255,0)
COLOR_CELESTE = (0,0,128)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Eventos de Pygame")
pantalla.fill(COLOR_CELESTE)
ingreso = ""
ingreso_rect = pygame.Rect(50, 50, 400, 50)
pygame.draw.rect(pantalla, COLOR_AMARILLO, ingreso_rect)
pygame.display.flip()
seguir = True
while seguir:
     lista_eventos = pygame.event.get()
     for evento in lista_eventos:
        if evento.type == pygame.QUIT:
           seguir = False
        elif evento.type == pygame.KEYDOWN: #presiono una tecla
              if evento.key == pygame.K_BACKSPACE:
                ingreso = ingreso[:-1]  # Eliminar el último carácter
              else:
                ingreso += evento.unicode
                
                
        if evento.type == pygame.KEYDOWN: #presiono una tecla        
             if evento.key == pygame.K_RETURN:  # Presiono Enter
                print(f"Texto ingresado: {ingreso}")
             # Dibujar el texto ingresado
        pantalla.fill(COLOR_CELESTE)
        pygame.draw.rect(pantalla, COLOR_AMARILLO, ingreso_rect)
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render(ingreso, True, COLOR_CELESTE)
        pantalla.blit(texto, (ingreso_rect.x + 5, ingreso_rect.y + 5))
        pygame.display.flip()

pygame.quit()
