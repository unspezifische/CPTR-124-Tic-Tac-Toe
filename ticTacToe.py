from turtle import *
from math import sqrt
from tttlogic import *
from tkinter import messagebox

currentPlayer = 'X'            ## 'X' goes first (can be commented out if player's wish to choose who goes first each game
canvas = getcanvas()
canvas.config(cursor="X_cursor")

# These three variables are used to determine the position and size of the TicTacToe grid
gridSize = 75
startX = -225
startY = 125

x = None
y = None

#hideturtle()
tracer(0)
title('Tic-Tac-Toe')
bgcolor('ghost white')


def setup():
#    currentPlayer = None    ## Only used if the players wish to determine first move each game
    clear()            ## Clear all previous drawings (necessary to reset the board)
    penup()
    pensize(4)
    setposition(startX + gridSize, startY)        ## Set turtle in position to draw vertical lines
    setheading(270)                               ## Ensure proper heading
    pencolor('systemBlack')           ## Set pencolor to black (necessary when resetting the board)
    pendown()

    for i in range(2):                ## Draws veritcal lines
        forward(gridSize * 3)
        penup()
        setposition(xcor() + gridSize,startY)
        pendown()

    penup()
    setposition(startX,startY - gridSize)    ## Set turtle in position to draw horizontal lines
    setheading(0)                            ## Ensure proper heading
    pendown()

    for i in range(2):                ## Draws horizontal lines
        forward(gridSize * 3)
        penup()
        setposition(startX,ycor()-gridSize)
        pendown()

    update()
    initialize_board()


# Returns the x, y position of the onscreen click
def mouse_clicked(x, y):
    squareID = point_to_square(x, y)    ## Determine the squareID of the user's click

    if current_player() == 'X':            ## If the currentPlayer is 'X', draw an 'X' and chagne currentPlayer to 'O'
        drawX(squareID)
        
    elif current_player() == 'O':          ## If the currentPlayer is 'O', draw an 'O' and chagne currentPlayer to 'X'
        drawO(squareID)
    
    winning_scenario()


# Determine the square the user selected
def point_to_square(x,y):
    '''
    Each logic statement checks the x, y values passed to the function
    against the range of x, y values for each square in the TicTacToe grid
    '''
    if startX < x < startX + gridSize and startY - gridSize < y < startY:
        return "NorthWest"
        
    elif startX + gridSize < x < startX + 2*gridSize and startY - gridSize < y < startY:
        return "North"
    
    elif startX + 2*gridSize < x < startX + 3*gridSize and startY - gridSize < y < startY:
        return "NorthEast"
        
    elif startX < x < startX + gridSize and startY - 2*gridSize < y < startY - gridSize:
        return "West"
    
    elif startX + gridSize < x < startX + 2*gridSize and startY - 2*gridSize < y < startY - gridSize:
        return "Center"
    
    elif startX + 2*gridSize < x < startX + 3*gridSize and startY - 2*gridSize < y < startY - gridSize:
        return "East"
        
    elif startX < x < startX + gridSize and startY - 3*gridSize < y < startY - 2*gridSize:
        return "SouthWest"
        
    elif startX + gridSize < x < startX + 2*gridSize and startY - 3*gridSize < y < startY - 2*gridSize:
        return "South"
        
    elif startX + 2*gridSize < x < startX + 3*gridSize and startY - 3*gridSize < y < startY - 2*gridSize:
        return "SouthEast"


# Accepts the string identifing a specific square and returns the (x, y) position of it's corner
def square_to_point(squareID):            
    global x, y
    
    if squareID == 'NorthWest':
        x = startX
        y = startY
    
    elif squareID == 'North':
        x = startX + gridSize
        y = startY
        
    elif squareID == 'NorthEast':
        x = startX + 2*gridSize
        y = startY
        
    elif squareID == 'West':
        x = startX
        y = startY - gridSize
        
    elif squareID == 'Center':
        x = startX + gridSize
        y = startY - gridSize
        
    elif squareID == 'East':
        x = startX + 2*gridSize
        y = startY - gridSize
        
    elif squareID == 'SouthWest':
        x = startX
        y = startY - 2*gridSize
        
    elif squareID == 'South':
        x = startX + gridSize
        y = startY - 2*gridSize
    
    elif squareID == 'SouthEast':
        x = startX + 2*gridSize
        y = startY - 2*gridSize
    else:
        x = None
        y = None
        
    return (x,y)


# Accepts the string of a square, runs square_to_point, then draws an 'X' in the appropriate square
def drawX(squareID):
    penup()
    pencolor('RoyalBlue2')
    s = square_to_point(squareID)    
    if look(squareID) == None and s != (None, None):
        move(squareID)
        setpos(square_to_point(squareID))           ## Set position to corner of square
        setheading(-45)                             ## Set proper heading
        pendown()
        forward(sqrt(gridSize**2+gridSize**2))      ## Go forward the diagonal length of the grid
        penup()
        setpos(xcor(),ycor()+gridSize)              ## Set new position for second line of 'X'
        setheading(-135)                            ## Set proper heading
        pendown()
        forward(sqrt(gridSize**2+gridSize**2))      ## Go forward the diagonal length of the grid
        update()
        turnO()                                     ## This will change the screen so that the players know who's turn it is                        
    else:
        pass


# Accepts the string of a square, runs square_to_point, then draws a blue circle
def drawO(squareID):
    penup()
    pencolor('MediumVioletRed')
    corner = square_to_point(squareID)
    s = square_to_point(squareID)
    if look(squareID) == None and s != (None, None):
        move(squareID)
        setpos(corner)                              ## Set position to corner of square
        setpos(xcor(),ycor() - gridSize/2)          ## Adjust turtle's position to draw circle
        setheading(-90)                             ## Set proper heading
        pendown()
        circle(gridSize/2)                          ## Draw a circle with diameter of gridSize
        update()                                    ## Update canvas
        turnX()                                     ## Changes the screen to show current player's cursor
    else:
        pass

    
# Changes currentPlayer to 'X' when the user clicks the 'x' key and changes window title to reflect change
def turnX():
    global currentPlayer, canvas
    canvas.config(cursor="X_cursor")
    title('Turn: Player X')
    color('black')
    update()

# Changes currentPlayer to 'O' when the user clicks the 'o' key and changes window title to reflect change
def turnO():
    global currentPlayer, canvas
    canvas.config(cursor="circle")
    title('Turn: Player O')
    color('black')
    update()


# Uses the check_status() function of the GameEngine to detect a winning scenario. Resets the board when there is a win.
def winning_scenario():
    if check_status() != (None, 'Playing'):            ## If the game is over (not still playing)
        winner = check_status()                ## Saves the return tuple
        if winner == (None, 'Draw'):           ## Special case for games that end in "Draw"
            winner = 'Draw'
        else:
            direction = winner[1]
            
            startpos = direction[4:6]
            endpos = direction[7:9]
            
            print(direction)
            print(startpos)
            print(endpos)
            
            if startpos == 'NW':
                startpos = 'NorthWest'
            elif startpos == 'N_':
                startpos = 'North'
            elif startpos == 'NE':
                startpos = 'NorthEast'
            elif startpos == 'W_':
                startpos = 'West'
            elif startpos == 'SW':
                startpos = 'SouthWest'
            
            print(startpos)
            print(square_to_point(startpos))
            if startpos == 'North':
                endpos = 'South'
            elif startpos == 'West':
                endpos = 'East'
            else:
                if endpos == 'NE':
                    endpos = 'NorthEast'
                elif endpos == 'SW':
                    endpos = 'SouthWest'
                elif endpos == 'SE':
                    endpos = 'SouthEast'
                  
            print(endpos)
            print(square_to_point(endpos))

            penup()
            pencolor('Black')
            pensize(6)
            setposition(square_to_point(startpos))
            pendown()
            setposition(square_to_point(endpos))
            update()
        
        messagebox.showinfo('Game Over' , winner)        ## Display information in messagebox
        setup()
        initialize_board()
    else:
        pass

setup()
title('Ready Player 1')
listen()
#onkeypress(turnX, key="x")
#onkeypress(turnO, key="o")
onkeypress(setup, key="q")
onscreenclick(mouse_clicked)

mainloop()