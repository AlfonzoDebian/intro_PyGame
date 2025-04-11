import pygame, sys

pygame.init()

PANTALLA = pygame.display.set_mode((727,898))
pygame.display.set_caption("Imagenes")
COLOR_NEGRO = pygame.Color(0, 0, 0)
PANTALLA.fill(COLOR_NEGRO)

# pygame.image.load carga una imagen guardada en el computador.
# convert() evita la lentitud en la ejecución del juego, al cargar una imagen.
selfie = pygame.image.load("img/mario03.png").convert()

# ubicar la imagen en una coordenda, la esquira sup. izq. de la imagen.
PANTALLA.blit(selfie, (100, 100))

# BUCLE DE JUEGO
while 1:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.flip()