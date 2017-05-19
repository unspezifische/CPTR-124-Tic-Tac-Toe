from turtle import *
from tkinter import messagebox 
from math import sqrt
hideturtle()
speed(0)
tracer(0)


currentplayer = "x"
canvas = getcanvas()

def grid():
    """ Draws playing grid """
    pensize(5)
#horizontal lines
    penup()
    goto(-150,50)
    pendown()
    forward(300)
    penup()
    goto(-150,-50)
    pendown()
    forward(300)
    penup()
    goto(0,0)
    
#vertical lines
    goto(-50,150)
    right(90)
    pendown()
    forward(300)
    penup()
    goto(50, 150)
    pendown()
    forward(300)
    update()

def point_to_square(x, y):
    """ Maps square and returns the location as a string """
    if -150 <= x <= -50 and 50 <= y <= 150:
        return "NorthWest"
    if -150 <= x <= -50 and -50 <= y <= 50:
        return "West"
    if -150 <= x <= -50 and -150 <= y <= -50:
        return "SouthWest"
    if -50 <= x <= 50 and 50 <= y <= 150:
        return "North"
    if -50 <= x <= 50 and -50 <= y <= 50:
        return "Center"
    if -50 <= x <= 50 and -150 <= y <= -50:
        return "South"
    if 50 <= x <= 150 and 50 <= y <= 150:
        return "NorthEast"
    if 50 <= x <= 150 and -50 <= y <= 50:
        return "East"
    if 50 <= x <= 150 and -150 <= y <= -50:
        return "SouthEast"

def square_to_point(square):
    """ Maps a square to its location on the board.  Used to
        render a square in its proper place. """
    if square == "NorthWest":
        return -150, 150
    elif square == "North":
        return -50, 150
    elif square == "NorthEast":
        return 50, 150
    elif square == "West":
        return -150, 50
    elif square == "Center":
        return -50, 50
    elif square == "East":
        return 50, 50
    elif square == "SouthWest":
        return -150, -50
    elif square == "South":
        return -50, -50
    elif square == "SouthEast":
        return 50, -50
    
def mouseclick (x, y):
    """ Allows player to click on the screen and play an X or an O """
    print(str(x) + "," + str(y) + "\n" + str(point_to_square(x,y)))
    point_to_square(x,y)
    print(square_to_point(point_to_square(x,y)))
    if currentplayer == "x":
        drawx(point_to_square(x,y))
    if currentplayer == "o":
        drawo(point_to_square(x,y))
        
    
def drawx(squarename):
    """ Draws X """
    pensize(3)
    pencolor("LightCoral")
    penup()
    setposition(square_to_point(squarename))
    setheading(-45)
    forward(30)
    pendown()
    forward(89)
    penup()
    setposition(xcor() - 70, ycor())
    setheading(43)
    forward(2)
    pendown()
    forward(89)
    update()
    
def drawo(squarename):
    """Draws O """
    pensize(3)
    pencolor("LightBlue")
    penup()
    setposition(square_to_point(squarename))
    setposition(xcor() + 50, ycor() - 9)
    pendown()
    setheading(0)
    circle(-40)
    update()
    
def turnx():
    global currentplayer
    currentplayer = "x"
    title("Player X")
    canvas.config(cursor="X_cursor")
    
def turno():
    global currentplayer
    currentplayer = "o"
    title("Player O")
    canvas.config(cursor="circle")
    
    
    
    
    
grid()
listen()
onscreenclick(mouseclick)
onkeyrelease(turnx, "x")
onkeyrelease(turno, "o")
mainloop()