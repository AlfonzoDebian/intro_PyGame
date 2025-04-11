import pygame
import sys

pygame.init()

# Colores
xmorado = (128, 0, 128)
xazul = (135, 206, 235)
xverde = (144, 238, 144)
xgris = (163, 163, 163)
colorllantas = (128, 158, 158)
xnegro = (0, 0, 0)
xamarillo = (255, 255, 0)
xrojo = (255, 0, 0)

# Ventana dimensiones
juegov = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Homer Dask")

clock = pygame.time.Clock()

# Variables para el sol
radio = 50  # Radio inicial del sol
cambio_radio = 2  # Velocidad de cambio del tamaño

# Variables para el humo
humo = [(250, 140), (230, 120), (210, 100)]

while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    juegov.fill(xazul)

    # Fondo y vías
    pygame.draw.rect(juegov, xverde, (0, 400, 600, 200))  # Pasto
    for i in range(0, 500, 50):  # Vías del tren
        pygame.draw.line(juegov, xnegro, (i, 380), (i + 50, 380), 5)
    pygame.draw.rect(juegov, xgris, (0, 375, 500, 5))  # Base de las vías

    # Vagones y chimenea
    pygame.draw.rect(juegov, xgris, (150, 260, 200, 100))  # Vagón principal
    pygame.draw.rect(juegov, xgris, (250, 160, 100, 100))  # Cabina superior
    pygame.draw.rect(juegov, xrojo, (250, 130, 20, 30))  # Chimenea

    # Humo
    for i in range(len(humo)):
        pygame.draw.circle(juegov, xgris, humo[i], 20)
        humo[i] = (humo[i][0], humo[i][1] - 1)  # Mover el humo hacia arriba
        if humo[i][1] < 0:  # Reiniciar humo cuando salga de la pantalla
            humo[i] = (humo[i][0], 140)

    # Llantas
    pygame.draw.circle(juegov, colorllantas, (300, 360), 50)
    pygame.draw.circle(juegov, colorllantas, (200, 360), 50)

    # Cara (decorativa)
    pygame.draw.circle(juegov, xamarillo, (300, 210), 50)
    pygame.draw.circle(juegov, xnegro, (280, 200), 10)  # Ojo izquierdo
    pygame.draw.circle(juegov, xnegro, (320, 200), 10)  # Ojo derecho
    pygame.draw.rect(juegov, xnegro, (287, 220, 30, 10))  # Boca

    # Bandera
    pygame.draw.rect(juegov, xrojo, (270, 100, 60, 20))  # Bandera roja
    pygame.draw.line(juegov, xnegro, (270, 100), (270, 130), 3)  # Palo de la bandera

    # Sol
    radio += cambio_radio
    if radio >= 60 or radio <= 50:
        cambio_radio = -cambio_radio
    pygame.draw.circle(juegov, xamarillo, (120, 100), radio)

    # Frontral
    pygame.draw.rect(juegov, xnegro, (120,360, 20, 90))

    # Sistemas de fuentes
    fontarial = pygame.font.SysFont("Arial", 35, True, True)
    fontarialdos = pygame.font.SysFont("Arial", 20, True, True)
    textouno = fontarial.render("Colegio Guanenta", True, xmorado)
    textodos = fontarialdos.render("Especialidad Sistemas 2025", True, xmorado)
    textoname = fontarialdos.render("Alfonzo", True, xmorado)
    juegov.blit(textodos, (110, 100))
    juegov.blit(textouno, (100, 50))
    juegov.blit(textoname, (0, 480))

    pygame.display.flip()
