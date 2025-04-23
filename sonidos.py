import pygame
import sys

# Inicializar los odulos
pygame.init()
pygame.mixer.init()

#colores
COLOR_BLANCO = pygame.Color(255,255,255)

# ventana
PANTALLA = pygame.display.set_mode((400,400))
PANTALLA.fill(COLOR_BLANCO)
pygame.display.set_caption("sonidos:)")

CONTINUAR = True

#sonido de fondo
SILBATO = pygame.mixer.music.load("sounds/silbato.ogg")
pygame.mixer.music.play(1,0.0)
#Añadir una imagen.
imagen_fondo = pygame.image.load("./img/images.jpeg")
# efectos sonoros
GALLO = pygame.mixer.Sound("sounds/gallo.ogg")
CUERVO = pygame.mixer.Sound("sounds/cuervo.ogg")
BICI = pygame.mixer.Sound("sounds/timbre.ogg")


while CONTINUAR:
    # cierra a ventana si se hace click en  la x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CONTINUAR = False
    #detectar si oprimio una tecla
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                CONTINUAR == False
            elif event.key == pygame.K_o:
                GALLO.play()
            elif event.key ==pygame.K_c:
                CUERVO.play()
            elif event.key == pygame.K_v:
                BICI.play()
            elif event.key == pygame.K_DOWN:
                VOLUMEN = pygame.mixer.music.get_volum() - 0.1
                pygame.mixer.music.set_volume(VOLUMEN)
                GALLO.set_volume(VOLUMEN)
                CUERVO.set_volume(VOLUMEN)
                BICI.set_volume(VOLUMEN)
            elif event.key == pygame.K_UP:
                VOLUMEN = pygame.mixer.music.get_volum() + 0.1                
                pygame.mixer.music.set_volume(VOLUMEN)
        

        # agregar mi foto.
        PANTALLA.blit(imagen_fondo, (100, 90))
        pygame.display.update()

               

pygame.display.flip()