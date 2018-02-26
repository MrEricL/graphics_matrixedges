from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    mlen = len(matrix[0])
    i = 0

    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    while (i < mlen):
        #print i
        x1 = matrix[0][i]
        y1 = matrix[1][i]
        x2 = matrix[0][i+1]
        y2 = matrix[1][i+1]
        #print x1,y1,x2,y2
        draw_line(x1,y1,x2,y2, screen, color)
        i+= 2


def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)

def slope(x0, y0, x1, y1):
    if (x0-x1 == 0):
        return False

    else:
        rise = float(y1) - float(y0)
        run = float(x1) - float(x0)
        slp = rise / run
        #Oct 1/5
        if ((slp > 0) and (slp <= 1)):
            return 1

        #Oct 2/6
        elif slp > 1:
            return 2

        #Oct 3/7
        elif slp < -1:
            return 3
        #Oct 4/8
        elif ((slp >= -1) and (slp < 0)):
            return 4

        else:
            return False


    
def draw_line( x0, y0, x1, y1, screen, color ):

    x = x0
    y = y0
    A = y1-y0
    B = -(x1-x0)
    m = slope (x, y, x1, y1)


    #Special Vert / Hor

    if (B == 0):
        while (y <= y1):
            plot(screen,color,x,y)
            y+=1
    elif (A == 0):
        while (x <= y1):
            plot(screen,color,x,y)
            x+=1

    #Oct 1

    elif (m == 1):

        d = 2 * A + B
        while (x <= x1):
            plot(screen,color,x,y)

            if (d > 0):
                y+=1
                d+= 2*B
            x+=1
            d+=2*A

    #Oct 2

    elif (m == 2):
        d = 2 * B + A
        while (y<=y1):
            plot(screen,color,x,y)

            if (d < 0):
                x+=1
                d+= 2*A
            y+=1
            d+=2*B      

    #Oct 8

    elif (m == 4):
        d = 2 * A - B
        while (x<=x1):
            plot(screen,color,x,y)

            if (d < 0):
                y-=1
                d-= 2*B
            x+=1
            d+=2*A  
    #Oct 7

    elif (m == 3):
        d = A-(2*B)
        while (y>=y1):
            plot(screen,color,x,y)

            if (d > 0):
                x+=1
                d+= 2*A
            y-=1
            d-=2*B  
    else: 
        print "something is wrong"
