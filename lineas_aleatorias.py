import pygame
import sys
import random

pygame.init()

Negro = (0, 0, 0)
MoradoDebian = (191, 64, 191)
blanco = (255, 255, 255)

posicion1 = random.randint(100, 350)

juego = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Lineas Randoms")

clock = pygame.time.Clock()



while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    juego.fill(Negro)

#   Sistemas De Rectangulo 
    pygame.draw.rect(juego, MoradoDebian, (90, 120, 300, 290), 1)

#   Crear lineas aleatorias
# 
    ColorRandom = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  

    
    posicion1 = random.randint(100, 350)
    posicion2 = random.randint(100, 380)
    pygame.draw.line(juego, ColorRandom, (posicion1, 130), (posicion2, 400))
  
#   Sistemas de texto.
    textoj = pygame.font.SysFont("Arial", 25, True, True)
    texto = textoj.render("Colegio San Jose Del Guanenta", True, blanco)
    especialidadtext = textoj.render("Especialidad: Sistemas", True, blanco)
    textoname = textoj.render("MrDebian 10-5", True, blanco)
    juego.blit(textoname, (160, 430))
    juego.blit(texto, (50, 50))
    juego.blit(especialidadtext,(90, 80))


    pygame.display.flip()