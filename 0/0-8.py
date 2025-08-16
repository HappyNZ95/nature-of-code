from p5 import *
import numpy as np

WIDTH = 640
HEIGHT = 360

def setup():
    size(WIDTH, HEIGHT)
    no_loop()

def draw():
    # Create a random grayscale array
    arr = np.random.randint(0, 256, (HEIGHT, WIDTH), dtype=np.uint8)

    # Expand to RGB (grayscale) and alpha channel
    img_array = np.stack([arr, arr, arr, 255 * np.ones_like(arr)], axis=2)

    # Create a p5 image and assign the array to pixels
    img = create_image(WIDTH, HEIGHT)
    img.pixels = img_array

    # Draw the image
    image(img, 0, 0)

run()
