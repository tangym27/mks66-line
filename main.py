from display import *
from draw import *

screen = new_screen()
color = 15

def structure():
    color = 15
    for i in range(500):
        draw_line(i, 0, i, 500, screen, [202,207,209])
    for i in range(15):
        # makes the horizontal bars
        draw_line( 50, 175 + i , 430 , 175 + i, screen, [255-color,color ,255])
        draw_line( 50 , 325 + i , 430 , 325 + i, screen, [255-color,color ,255])
        #makes vertical
        draw_line( 165 + i , 50  , 165 +i, 450 , screen, [255-color,color ,255])
        draw_line( 305 + i , 50  , 305 +i, 450 , screen, [255-color,color ,255])
        color += 15

# fills in the front fow
def front(offset, shape):
    color = 0
    x = offset
    if (shape == "diamond"):
        for i in range(10):
            draw_line( x , 370-i-i  , x, 421 +i+i, screen, [53, 158, 106+color])
            color += 10
            x+=3
        for i in range(11):
            draw_line( x , 350 +i + i  , x, 441 - i -i, screen, [53, 158, 106+color])
            x+=3
            color -= 10
    if (shape == "x"):
        for i in range(10):
            draw_line( offset , 370-i-i  , offset + 70, 421 +i+i, screen, [64,199,249])
            color += 10
            draw_line( offset , 421 +i+i , offset + 70, 370-i-i, screen, [255-color,color ,255])
            color -= 10

# fills in the middle row
def middle(offset, shape):
    x = offset
    color =  0
    if (shape == "diamond"):
        for i in range(10):
            draw_line( x , 230-i-i  , x, 281 +i+i, screen, [160+color,96+color,255])
            x+=3
            color += 8
        for i in range(11):
            draw_line( x , 210 +i + i  , x, 301 - i -i, screen, [160+color,96+color,255])
            x+=3
            color -= 8
    if (shape == "x"):
        for i in range(10):
            draw_line( offset , 230-i-i  , offset + 70, 281 +i+i, screen, [64,199,249])
            draw_line( offset , 281 +i+i , offset + 70, 230-i-i, screen, [255-color,color ,255])

# fills in the bottom row
def bottom(offset, shape):
    x = offset
    color = 0
    if (shape == "diamond"):
        for i in range(10):
            draw_line( x , 80-i-i  , x, 131 +i+i, screen, [21+color, 255, 255])
            x+=3
            color += 10
        for i in range(11):
            draw_line( x , 60 +i + i  , x, 151 - i -i, screen, [21+color, 255, 255])
            x+=3
            color -= 10
    if (shape == "x"):
        for i in range(10):
            draw_line( offset , 80-i-i  , offset + 70, 131 +i+i, screen, [64,199,249])
            draw_line( offset , 131 +i+i , offset + 70, 80-i-i, screen, [255-color,color ,255])

# Testing all of the octants
def test():
    print("1")
    draw_line( 250 , 250 , 400,  300, screen, [255-color,color ,255])
#o2
    print("2")
    draw_line( 250 , 250 , 300,  400, screen, [255-color,color ,255])
#o3
    print("3")
    draw_line( 200 , 400 , 250,  250, screen, [255-color,color ,255])
#o4
    print("4")
    draw_line( 250 , 250 , 50,  300, screen, [255-color,color ,255])
#o5
    print("5")
    draw_line( 250 , 250 , 50,  200, screen, [255-color,color ,255])
#o6
    print("6")
    draw_line( 250 , 250 , 200,  100, screen, [255-color,color ,255])

#o7
    print("7")
    draw_line( 250 , 250 , 300,  50, screen, [255-color,color ,255])
#o8
    print("8")
    draw_line( 250 , 250 , 400,  200, screen, [255-color,color ,255])
    print ("undefined/0")
    draw_line( 250 , 250 , 100,  250, screen, [255-color,color ,255])
    draw_line( 250 , 250 , 450,  250, screen, [255-color,color ,255])
    draw_line( 250 , 250 , 250,  450, screen, [255-color,color ,255])
    draw_line( 250 , 450 , 250,  250, screen, [255-color,color ,255])



structure()
front(75, "diamond")
front(210, "x")
front(353, "diamond")

middle(70, "x")
middle(213, "diamond")
middle(353, "diamond")

bottom(70, "x")
bottom(213, "diamond")
bottom(353, "x")

display(screen)
save_extension(screen, 'img.png')
