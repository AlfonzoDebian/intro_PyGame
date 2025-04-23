import pygame
import sys

#
pygame.init()
pygame.mixer.init()

# colores
color_blanco = (255, 255, 255)


PANTALLA = pygame.display.set_mode((400, 400))
PANTALLA.fill(color_blanco)
pygame.display.set_caption("Sonido en pygame. ")


CONTINUAR = True


SILBATO = pygame.mixer.music.load("sound/silbato.ogg")
pygame.mixer.music.play(1, 0.0)

GALLO = pygame.mixer.Sound("sound/gallo.ogg")
CUERVO = pygame.mixer.Sound("sound/cuervo.ogg")

BICI = pygame.mixer.Sound("sound/timbre.ogg")



while CONTINUAR:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CONTINUAR = False
        elif event.type == pygame.KEYDOWN:
            pass  
