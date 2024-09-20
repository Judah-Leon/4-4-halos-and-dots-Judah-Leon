from PIL import Image, ImageDraw
from math import sqrt
import random
def distance_halo(image_name, targetx, targety, modifier):
    image = Image.open(image_name)
    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            red = pixels[x, y][0]
            green = pixels[x, y][1]
            blue = pixels[x, y][2]
            mod = int(sqrt((targetx - x)**2 + (targety - y)**2) / modifier)
            pixels[x, y] = (red - mod, green - mod, blue - mod)
    image.save(image_name[:-4] + '_halo.png')
# distance_halo('dreamy.png', 450, 300, 3)

def pointillism(image_name):
    image = Image.open(image_name)
    pixels = image.load()
    canvas = Image.new("RGB",(image.size[0],image.size[1]), "white")

    for run in range(1000000):
        x = random.randint(0, image.width - 1)
        y = random.randint(0, image.height - 1)
        size = random.randint(15, 20)
        ellipsebox=[(x,y),(x+size,y+size)]
        draw = ImageDraw.Draw(canvas)
        draw.ellipse(ellipsebox,fill=(pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]))
        del draw
    canvas.save(image_name[:-4] + '_pointillised.png')
pointillism('dreamy.png')