import pygame
import math
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
surface = pygame.Surface((1280, 720), pygame.SRCALPHA)
clock = pygame.time.Clock()
running = True

walker_default_colour = (0,15,125,20)

class Walker():
    def __init__(self):
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.size = 30
        self.colour = walker_default_colour

    def step(self):
        #stepx = (random.random() ** 2) * random.choice([-1, 1]) * self.size # favour small steps 
        #stepy = (random.random() ** 2) * random.choice ([-1, 1]) * self.size  # favour small steps
        stepx = math.sqrt(random.random()) * random.choice([-1, 1]) * self.size # favour large steps
        stepy = math.sqrt(random.random()) * random.choice ([-1, 1]) * self.size # favour large steps
        self.x += stepx
        self.y += stepy
        pygame.draw.circle(surface, self.colour, (int(self.x), int(self.y)), self.size)
        

walker = Walker()

frame_count = 0

screen.fill("white")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    frame_count += 1

    if frame_count % 25 == 0:
        walker.step()

    screen.blit(surface,(0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
