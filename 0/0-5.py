import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Walker():
    def __init__(self):
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.size = 12
        self.colour = 1

    def step(self):
        random_number = random.random()
        self.colour += 1000

        if random_number < 0.5:
            self.x -= random.gauss(0, 50)
            pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)
        else:
            self.y += random.gauss(0, 50)
            pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)

walker = Walker()

frame = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("black")

    frame += 1

    if frame % 5 == 0:
        walker.step()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
