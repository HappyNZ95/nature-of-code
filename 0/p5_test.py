from p5 import *
import random

WIDTH = 1920
HEIGHT = 1080

def setup():
    size(WIDTH, HEIGHT)
    background(255)


class Walker():

    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.tx = 0
        self.ty = 10000

    def step(self):
        self.x = remap(noise(self.tx), (0, 1), (0, WIDTH))
        self.y = remap(noise(self.ty), (0, 1), (0, HEIGHT))
        self.tx += 0.01
        self.ty += 0.01

    def show(self):
        stroke(0)
        ellipse(self.x, self.y, 34, 34)


walker = Walker()

def draw():
    walker.step()
    walker.show()

run()
