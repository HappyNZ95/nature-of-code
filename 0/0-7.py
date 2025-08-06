import pygame
from noise import pnoise1

def map(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

walker_default_colour = (0,0,0,50)

class Walker():
    def __init__(self):
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.tx = 1
        self.ty = 10000
        self.size = 30
        self.colour = walker_default_colour

    def step(self):

        self.x = map(pnoise1(self.tx), -1, 1, 0, screen.get_width())
        self.y = map(pnoise1(self.ty), -1, 1, 0, screen.get_height())

        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size)

        self.tx += 0.01
        self.ty += 0.01
        

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


    screen.fill("white")
    walker.step()


   # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
