import pygame
import random

# Inicializamos los módulos de pygame.
pygame.init()

rojo = random.randint(0, 255)
verde = random.randint(0, 225)
azul = random.randint(0, 225)

# Establecer título
pygame.display.set_caption("didier.py")

# Hacemos el tamaño de la ventana
ventana = pygame.display.set_mode((400, 400))

# Definimos el color
azul = (rojo, verde, azul)

# Crear una superficie
azul_superficie = pygame.Surface((200, 200))  # Corregido: Se usa una tupla para el tamaño

# Rellenar la superficie de azul
azul_superficie.fill(azul)

# Inserto o muevo la superficie en la ventana
ventana.blit(azul_superficie, (100, 100))

# Actualiza la ventana
pygame.display.flip()

# Bucle
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()
