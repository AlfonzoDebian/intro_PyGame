import pygame, sys
import math
PI = math.pi

pygame.init()

# VENTANA DE 400 POR 400 CON UN FONDO NEGRO
PANTALLA = pygame.display.set_mode((500,600))
pygame.display.set_caption("Transformaciones")
COLOR_NEGRO = pygame.Color(0, 0, 0)
PANTALLA.fill(COLOR_NEGRO)

#Image
logo = pygame.image.load("img/escudoColegio.png").convert()
PANTALLA.blit(logo, (50, 50))

# Flip: simetría axial
logoFlip = pygame.transform.flip(logo, True, True)
PANTALLA.blit(logoFlip, (150, 183))

# Rotate: girar 30 grados la imagen
logoRotate = pygame.transform.rotate(logo, 30)
PANTALLA.blit(logoRotate, (250, 250))

# Scale: aumentar dos veces la imagen
logoScale = pygame.transform.scale2x(logo)
PANTALLA.blit(logoScale, (50, 350))

color = pygame.transform.average_color(logo)
print(color)

# BUCLE DE JUEGO
while 1:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.flip()