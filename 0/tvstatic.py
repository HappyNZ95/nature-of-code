import pygame
import random
from noise import pnoise2

def map_value(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

WIDTH, HEIGHT = 1920, 720

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(WIDTH):
        for y in range(HEIGHT):
           screen.set_at((x,y), (random.randint(1,255),random.randint(1,255),random.randint(1,255)))


    pygame.display.flip()
    clock.tick(30)

pygame.quit()

