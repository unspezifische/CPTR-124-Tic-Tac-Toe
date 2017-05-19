"""
ttt_logic
  This module contains the logic to drive a two-player Tic-Tac-Toe
  game.
"""

#---------------------------------------------------------------
#  Define any global variables this module may need to maintain the
#  state of a Tic-Tac-Toe game.
#---------------------------------------------------------------
NorthWest = None   # Top, left square
North = None       # Top, middle square
NorthEast = None   # Top, right square
West = None        # Left, middle square
Center = None      # Center square
East = None        # Right, middle square
SouthWest = None   # Bottom, left square
South = None       # Bottom, middle square
SouthEast = None   # Bottom, right square

currentPlayer = 'X'


def check_status():
    """
    Checks to see if either player has won or if the board is filled.  
    Returns a two-tuple in which the first component is the string
    "X" or the string "O" or the value None; the second component
    of the tuple is one of the following strings that indicates the
    Tic-Tac-Toe board's status:
      "Playing"     No one has won and a move is available
      "Win_NW_NE"   Win across top row
      "Win_W_E"     Win across middle row
      "Win_SW_SE"   Win across bottom row
      "Win_NW_SW"   Win along left colunm
      "Win_N_S"     Win along center column
      "Win_NE_SE"   Win along right column
      "Win_NW_SE"   Win from left-top corner to right-bottom 
      "Win_NE_SW"   Win from right-top corner to left-bottom 
      "Draw"        All squares filled with no winner
    The first component of the resulting tuple represents the game
    winner, and the second component of the tuple represents the
    winning configuration.  If the status component is "Playing" or
    "Draw", the winner component should be None; for example, the
    tuple ("X", "Win_NE_SE") would be a valid return value, but
    neither ("X", "Draw") nor ("O", "Playing") represents a valid
    result. 
    """
    if North != None and NorthWest == North == NorthEast:
      return North, "Win_NW_NE"
    elif Center != None and West == Center == East:
      return Center, "Win_W_E"
    elif South != None and SouthWest == South == SouthEast:
      return South, 'Win_SW_SE'
    elif West != None and NorthWest == West == SouthWest:
      return West, 'Win_NW_SW'
    elif Center != None and North == Center == South:
      return Center, 'Win_N_S'
    elif East != None and  NorthEast == East == SouthEast:
      return East, 'Win_NE_SE'
    elif Center != None and NorthWest == Center == SouthEast:
      return Center, 'Win_NW_SE'
    elif Center != None and NorthEast == Center == SouthWest:
      return Center, 'Win_NE_SW'
    elif NorthWest != None and North != None and NorthEast != None and West != None and Center != None and East != None and SouthWest != None and South != None and SouthEast != None:
      return None, 'Draw'
    else:
      return None, "Playing"   # Replace with your implementation


def move(location):
    global currentPlayer, NorthWest, North, NorthEast, West, Center, East, SouthWest, South, SouthEast
    """
    Places the current player's mark at the given location, if possible.
    The caller must pass one of the following strings specifying
    the location:
      "NorthWest"   Top, left square
      "North"       Top, middle square
      "NorthEast"   Top, right square
      "West"        Left, middle square
      "Center"      Center square
      "East"        Right, middle square
      "SouthWest"   Bottom, left square
      "South"       Bottom, middle square
      "SouthEast"   Bottom, right square

    Returns True if the specified location is available (that is,
    the global variable keeping track of that position is None);
    otherwise the function returns False for an illegal move.
    If the current player makes a valid move, the function ensures
    that control passes to the other player; otherwise, the move
    function does not affect the current player.
    """
    
    lastMove = currentPlayer
    
    if location == "NorthWest" and NorthWest == None:
      NorthWest = lastMove
      change_player()
      return True
      
    elif location == "North" and North == None:
      North = lastMove
      change_player()
      return True
      
    elif location == "NorthEast" and NorthEast == None:
      NorthEast = lastMove
      change_player()
      return True
      
    elif location == "West" and West == None:
      West = lastMove
      change_player()
      return True
      
    elif location == "Center" and Center == None:
      Center = lastMove
      change_player()
      
      return True
      
    elif location == "East" and East == None:
      East = lastMove
      change_player()
      
      return True
      
    elif location == "SouthWest" and SouthWest == None:
      SouthWest = lastMove
      change_player()      
      return True
      
    elif location == "South" and South == None:
      South = lastMove
      change_player()
      return True
      
    elif location == "SouthEast" and SouthEast == None:
      SouthEast = lastMove
      change_player()
      return True
      
    else:
      return False
      
#    print('\nNorthWest:', NorthWest, '\nNorth:', North, '\nNorthEast:', NorthEast, '\nWest:', West, '\nCenter:', Center, '\nEast:', East, '\nSouthWest:', SouthWest, '\nSouth', South, '\nSouthEast', SouthEast)


def current_player():
    global currentPlayer
    """
    Returns the player whose turn it is to move.  This allows the
    presentation to report whose turn it is.
    Return value is one of either "X" or "O".
    """
    return currentPlayer


def set_player(new_player):
    global currentPlayer
    """
    Sets the current player.  Useful for games that require the
    player to answer a question correctly before a move.  If the
    player answers incorrectly, the turn moves to the opponent.
    Valid values for new_player are "X" or "O"; any other strings
    will not change the current player.
    """
    currentPlayer = new_player
    return currentPlayer     # Replace with your implementation


def change_player():
    global currentPlayer
    """
    Alternates turns between players.  X becomes O, and O becomes X.
    """
    if currentPlayer == 'X':
      currentPlayer = 'O'
      
    elif currentPlayer == 'O':
      currentPlayer = 'X'
    pass     # Replace with your implementation


def look(location):
    """
    Returns the mark at the given location.  The caller must pass 
    one of the following strings specifying the location:
      "NorthWest"   Top, left square
      "North"       Top, middle square
      "NorthEast"   Top, right square
      "West"        Left, middle square
      "Center"      Center square
      "East"        Right, middle square
      "SouthWest"   Bottom, left square
      "South"       Bottom, middle square
      "SouthEast"   Bottom, right square

    The function's valid return values are None, "X", or "O".
    Returns None if neither player has marked 
    the given location.  The function also returns None if the
    caller passes any string other than one of the location strings
    listed above.
    This function allows the presentation to draw the contents
    of the Tic-Tac-Toe board.
    """
    if location == 'NorthWest':
      return NorthWest
    elif location == 'North':
      return North
    elif location == 'NorthEast':
      return NorthEast
    elif location == 'West':
      return West
    elif location == 'Center':
      return Center
    elif location == 'East':
      return East
    elif location == 'SouthWest':
      return SouthWest
    elif location == 'South':
      return South
    elif location == 'SouthEast':
      return SouthEast

def initialize_board():
    global currentPlayer, NorthWest, North, NorthEast, West, Center, East, SouthWest, South, SouthEast
    """
    Make all the board locations empty and set current player to
    "X" (that is, reset the board to the start of a new game)
    """
    NorthWest = None   # Top, left square
    North = None       # Top, middle square
    NorthEast = None   # Top, right square
    West = None        # Left, middle square
    Center = None      # Center square
    East = None        # Right, middle square
    SouthWest = None   # Bottom, left square
    South = None       # Bottom, middle square
    SouthEast = None   # Bottom, right square

    currentPlayer = 'X'
    

if __name__ == "__main__":
    pass   #  This module is not meant to be run as a standalone program

