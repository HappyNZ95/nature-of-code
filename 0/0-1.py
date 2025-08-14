from p5 import *
import random

def setup():
    size(640, 240)
    background(255)


class Walker():

    def __init__(self):
        self.x = 640 / 2
        self.y = 240 / 2

    def show(self):
        stroke(0)
        point(self.x,self.y)

    def step(self):
        choice = floor(random.random())

        if choice < 0.25:
            self.x += 1
        elif choice < 0.5:
            self.x -= 1
        elif choice < 0.75:
            self.y += 1
        else:
            self.y -= 1

walker = Walker()

def draw():
    walker.step()
    walker.show()

run()
