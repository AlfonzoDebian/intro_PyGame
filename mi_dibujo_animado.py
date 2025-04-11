import pygame
import sys


pygame.init()

# Colores
xmorado = (128, 0, 128)

# Ventana dimenciones.
juegov = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Homer Dask")

clock = pygame.time.Clock()

while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#   sistemas de fuentes
    fontarial = pygame.font.SysFont("Arial", 35, True, True)
    fontarialdos = pygame.font.SysFont("Arial", 20, True, True)
    textouno = fontarial.render("Colegio Guanenta", True, xmorado)
    textodos = fontarialdos.render("Especialidad Sistemas 2025", True, xmorado)
    textoname = fontarialdos.render("Alfonzo", True, xmorado)
    juegov.blit(textodos, (110, 100))
    juegov.blit(textouno, (100, 50))
    juegov.blit(textoname, (0, 480))
    pygame.display.flip()