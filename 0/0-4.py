import pygame
import pygame_widgets
import random
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
surface = pygame.Surface((1280, 720), pygame.SRCALPHA)
screen.fill("white")
clock = pygame.time.Clock()
running = True

walker_default_colour = (0,125,125,15)

pygame.font.init()
font = pygame.font.SysFont('Arial', 30)



class Walker():
    def __init__(self, colour = walker_default_colour, x = screen.get_width() / 2, y = screen.get_height() / 2):
        self.x = x 
        self.y = y
        self.size = 15
        self.colour = colour

    def step(self, spread):
        self.x = random.gauss(640, spread) 
        pygame.draw.circle(surface, self.colour, (self.x, self.y), self.size)



walker = Walker()

slider = Slider(screen, 100, 100, 800, 40, min=0, max=500, step=1)
output = TextBox(screen, 475, 200, 100, 50, fontSize=30)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("black")

    spread_value = slider.getValue()

    output.setText(str(spread_value))

    walker.step(spread_value)
    screen.blit(surface,(0,0))

    pygame.draw.rect(screen, (255, 255, 255), (0,0,450,40))

    text_surface = font.render(f"Random gausian number: {str(round(walker.x))}", True, (0, 0, 0))
    screen.blit(text_surface, (1, 1)) # Blit the text Surface at coordinates (100, 100)

    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame_widgets.update(event)
    pygame.display.update()

    clock.tick(15)  # limits FPS to 60

pygame.quit()
