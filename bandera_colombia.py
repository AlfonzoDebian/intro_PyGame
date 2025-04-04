import pygame

pygame.init()

pygame.display.set_caption("COLOMBIA")

#Colores 
amarillo = (255, 255, 0)
azul = (0, 0, 255)
rojo = (255, 0, 0)

rojo_superfice = pygame.Surface((400, 100))
rojo_superfice.fill(rojo)

azul_superfice = pygame.Surface((400, 100))
azul_superfice.fill(azul)


amarillo_superficie = pygame.Surface((400, 200))
amarillo_superficie.fill(amarillo)

Ventana = pygame.display.set_mode((400, 400))
Ventana.blit(amarillo_superficie, (0,0))
Ventana.blit(azul_superfice, (0,200))
Ventana.blit(rojo_superfice, (0,300))


pygame.display.flip()



while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()