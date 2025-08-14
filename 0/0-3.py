import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

walker_default_colour = (50,50,50)
walkers=[]

class Walker():
    def __init__(self, colour = walker_default_colour, x = screen.get_width() / 2, y = screen.get_height() / 2):
        self.x = x 
        self.y = y
        self.size = 2
        self.colour = colour

        self.random_rgb_colour = (random.randint(1,255), random.randint(1,255), random.randint(1,255))


    def step(self):
        rgb_values = list(self.colour)
        for rgb_value in rgb_values:
            if rgb_value == 255:
                rgb_value = 1
            else:
                rgb_value += 10
        self.colour = tuple(rgb_values)



        random_number = random.random()

        if random_number >= 0.98 and len(walkers) < 150:
            new_walker = Walker(self.random_rgb_colour, random.randint(1, screen.get_width()), random.randint(1, screen.get_height()))
            walkers.append(new_walker)


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




    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
