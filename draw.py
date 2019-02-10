from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    x = x0
    y = y0

    if (x1-x0):
        y1= y1+ 0.0
        m = (y1-y0)/(x1-x0)
    else:
        m = 1.5 # to avoid an undefined error
        if (y1 < y0):
            draw_line( x0, y1, x1, y0, screen, color)

    # handles reflection (octant 3-6)
    if ((y1-y0) < 0):
        draw_line( x1, int(y1), x0, y0, screen, color)
    if ((x1-x0 < 0) and (y1 -y0 == 0)):
        draw_line( x1, int(y1), x0, y0, screen, color)
    if ((y1-y0 < 0) and (x1 -x0 == 0)):
        draw_line( x1, int(y1), x0, y0, screen, color)


    A = y1 - y0
    B = - (x1 - x0)
    if (abs(m) == 0.0): # no slope
        while (x <= x1):
            plot(screen, color, x, y)
            x += 1
    # OCTANT ONE
    if ((0 < m) and (m <= 1)):
        print("octant one "+ str(m))
        d = 2*A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y +=1
                d += 2*B
            x +=1
            d += 2*A
    # OCTANT TWO
    if ((0 < m) and (m > 1)):
        print("octant two: " +str (m))
        d = A + 2*B
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x +=1
                d += 2*A
            y +=1
            d += 2*B
    # OCTANT SEVEN
    if ((0 > m) and (m <= -1)):
        print("octant seven: " + str(m))
        d = A-2*B
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x +=1
                d += 2*A
            y -=1
            d -= 2*B
    #OCTANT EIGHT
    if ((0 > m) and (m > -1)):
        print("octant eight: " + str(m))
        d = 2*A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -=1
                d -= 2*B
            x +=1
            d += 2*A

    print ("slope:" + str(m))
