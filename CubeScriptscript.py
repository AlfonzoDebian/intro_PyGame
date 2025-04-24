import sys
import pygame

pygame.init()


ANCHO_VENTANA = 656
ALTO_VENTANA = 700
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))


pygame.display.set_caption("Cubo")

fondo = pygame.image.load("sprite/spritef/fondo.jpg")
spritecub = pygame.image.load("sprite/spritef/cuby.png")
spritecub = pygame.transform.scale(spritecub, (100, 100))


x = 290
y = 590
velocidad = 5 

Quit = True

while Quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit = False 

   
    keys = pygame.key.get_pressed()

   
    if keys[pygame.K_a] and x > 0:
        x -= velocidad  
    if keys[pygame.K_d] and x < ANCHO_VENTANA - 100:  
        x += velocidad  


    ventana.blit(fondo, (0, 0)) 
    ventana.blit(spritecub, (x, y))  

    pygame.display.update()

pygame.quit()



