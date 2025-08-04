import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

walkers=[]

class Walker():
    def __init__(self):
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.size = 25
        self.colour = 1

    def step(self):
        random_number = random.random()

        if random_number >= 0.98 and len(walkers) < 10:
            new_walker = Walker()
            walkers.append(new_walker)

        self.colour += 1000

        if random_number < 0.25:
            self.x -= self.size
            pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size) 
        elif random_number < 0.5:
            self.x += self.size
            pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size) 
        elif random_number < 0.75:
            self.y -= self.size
            pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size) 
        else:
            self.y += self.size
            pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)


walker = Walker()
walkers.append(walker)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("black")

    for walker in walkers:
        walker.step()
        print(walker)

    if len(walkers) == 10:
        walkers=[walker]



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 60

pygame.quit()
