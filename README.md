# 4.4-Halos-and-Dots
### Halos
Write a function that creates a dark halo around a choosen x and y coordinate. 
```pyhton
def distance_halo(image,targetX, targetY, modifier) :
    your code goes here
```

The distance_halo() functions works by calculating the distance for every pixel on the image to the pixel at (targetX, targetY). The distance is then divided by the modifier and the resulting value is then subtracted from the R,G,B values of each pixel on the image. 

Suggested steps( There is more than one way to solve this.)

1. Calculate the distance for each pixel to the pixel at (targetX, targetY) using the Pythagorean Theorem (a2 + b2 = c2). One will need to use the math.sqrt() function(https://www.tutorialspoint.com/python/number_sqrt.htm ).
![Pythagorean Theorem](images/distance_formula_pythagoras.gif)
2. Divide the distance by the modifier.
3. Calculate each pixel's new R,G, B values by subtracting the quotient.
 
Original
![Original](images/austin.jpg)

distance(atx,200,100,1)                                modifier = 1
![Modifier 1](images/mod1.png)

distance(atx, 200, 100, 2)                             modifier = 2      
![Modifier 2](images/mod2.png)

distance(atx, 200, 100, 3)                             modifier = 3
![Modifier 3](images/mod3.png)

 
### Pointilism
Create a function that converts a digital image to a pointilist image.
```python
def pointillism(image):
    your code goes here
```

The pointillism() function works by repeatedly taking the RGB values of random pixels on the image, and using the color values to draw colored circles on a new PIL image. 

Suggested Steps

1. Create a new PIL image by pasting the following code into your function:
```python
canvas = Image.new("RGB",(image.size[0],image.size[1]), "white")
```
2. Repeatedly select a random pixel from the image and take it's RGB values. This process should be repeated at least 5,000 times.
3. Each time a pixel's RGB values are taken, the color values should be used to draw a circle on the canvas image using the following code(copy/paste): 
```python
size = random.randint(3,5)
ellipsebox=[(x,y),(x+size,y+size)]
draw = ImageDraw.Draw(canvas)
draw.ellipse(ellipsebox,fill=(pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]))
del draw
```
 4. Create a new png file from the canvas image.
 
 Original
![Original](images/austin.jpg)

Pointilism
![Pointilism](images/austintest.png)