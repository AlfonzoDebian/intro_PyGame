import pygame
import sys
import random
import math

pygame.init()  # Esto inicializa todos los módulos de pygame

azul = (0, 0, 255)
rojo = (225, 0, 0)
rosado = (255, 192, 203)
negro = (0, 0, 0)
amarillo = (255, 255, 0)
blanco = (255, 255, 255)
n = (175, 0, 0)
color3 = (223, 143, 255)
PI = math.pi

ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Didier, SOTOS")

clock = pygame.time.Clock()

####### Bucle principal del juego

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(negro)

    # Dibujar líneas, polígonos, rectángulos, elipses y arco
    pygame.draw.line(ventana, rojo, (100, 100), (300, 300))
    pygame.draw.line(ventana, rojo, (100, 300), (300, 100))
    pygame.draw.lines(ventana, rojo, True, [(0, 0), (50, 100), (100, 50), (250, 250), (400, 400)])
    pygame.draw.lines(ventana, rosado, True, [(200, 0), (400, 200), (200, 400), (0, 200)])
    pygame.draw.polygon(ventana, amarillo, [(200, 200), (250, 300), (300, 350), (400, 350)], 1)
    pygame.draw.rect(ventana, rosado, (200, 200, 200, 100))
    pygame.draw.rect(ventana, rosado, (100, 100, 200, 200), 1)
    pygame.draw.circle(ventana, blanco, (300, 100), 100, 5)
    pygame.draw.ellipse(ventana, n, (100, 150, 200, 100), 3)
    pygame.draw.arc(ventana, color3, (300, 25, 180, 150), PI / 2, PI, 1)

    # **Agregar texto**
    fuente_arial = pygame.font.SysFont("Arial", 35, True, True)
    texto = fuente_arial.render("XDEBIAN", True, blanco)
    ventana.blit(texto, (50, 50))

    pygame.display.flip()
